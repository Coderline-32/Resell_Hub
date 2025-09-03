from django.shortcuts import render, redirect, get_object_or_404
from.forms import ProductListingForm
from django.contrib.auth.decorators import login_required
from users.models import SellerProfile
from .models import ProductListings
from .permissions import IsSellerOrReadOnly
from .serializers import ProductsSerializer, CategorySerializer, MyProductsSerializer
from rest_framework import generics, filters, permissions
from rest_framework.exceptions import PermissionDenied




# ------------------ API Views ------------------

# List all products with search and ordering functionality
class ProductsListView(generics.ListAPIView):
    queryset = ProductListings.objects.all().order_by("-created_at")
    serializer_class = ProductsSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description', 'category_name']
    ordering_fields = ['category__name', 'price', 'location', 'created_at' ]

    
    # Save a product with seller profile (only sellers can create)
    def perform_create(self, serializer):
        try:
            seller_profile = self.request.user.seller_profile
        except SellerProfile.DoesNotExist:
            raise PermissionError("You must be a seller to create products")
        
        serializer.save(seller=seller_profile)

# View single product details (read-only)
class ProductDetailView(generics.RetrieveAPIView):
    """
    GET: View a product (anyone can view)
    PUT/PATCH/DELETE: Only owner (seller) can update or delete
    
    """
    queryset = ProductListings.objects.all()
    serializer_class = ProductsSerializer

# Seller-specific products (list & create)    
class MyProductsView(generics.ListCreateAPIView):
    serializer_class = MyProductsSerializer
    permission_classes = [IsSellerOrReadOnly]

    # Return only products belonging to logged-in seller
    def get_queryset(self):
        user = self.request.user
        if not hasattr(user, 'seller_profile'):
            raise PermissionDenied("You are not a seller")
        return ProductListings.objects.filter(seller=user.seller_profile)
    
     # When creating product, assign seller automatically
    def perform_create(self, serializer):
        return serializer.save(seller=self.request.user.seller_profile)

# Seller-specific single product (view, update, delete)
class MyProductsDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MyProductsSerializer
    permission_classes = [IsSellerOrReadOnly] 

    def get_queryset(self):
        product_detail = ProductListings.objects.filter(seller=self.request.user.seller_profile)
        return product_detail
    
    
        

# ------------------ Template Views ------------------

# Create product via Django form
@login_required(login_url='users:index')
def create_product_view(request):

    try:
        seller_profile = request.user.seller_profile
    except SellerProfile.DoesNotExist:
        return redirect('products:home')
    
    if request.method == 'POST':
        form = ProductListingForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.posted_by = request.user.seller_profile
            product.save()
            return redirect('products:seller_dashboard')
    else:
        form = ProductListingForm()


    return render(request, 'products/create_product.html', {'form':form} )


# Seller dashboard showing only seller's products
@login_required
def seller_dashboard(request):
    try:
        seller_profile = request.user.seller_profile
    
    except SellerProfile.DoesNotExist:
        return redirect('products:home')
    
    products = ProductListings.objects.filter(seller=seller_profile)

    return render(request, 'products/seller_dashboard.html', {'products': products})

# Delete product (only if owned by seller)
@login_required
def delete_product(request, product_id):
    try:
        seller_profile = request.user.seller_profile

    except SellerProfile.DoesNotExist:
        return redirect('products:home')
    
    del_product = get_object_or_404(ProductListings, id= product_id, seller = seller_profile)
    
    if request.method == 'POST':
            del_product.delete()
            return redirect('products:seller_dashboard')
    
# Homepage: show all products and categories
def home_view(request):

    products = ProductListings.objects.all()
    categories = ProductListings.objects.values_list("category__name", flat=True).distinct()
    return render(request,  'products/home.html', {
                                                   'products': products,
                                                   'categories': categories
                                            
                                                    })


# Single product detail page
def product_detailed_view(request, product_id):
    product = get_object_or_404(ProductListings, id=product_id)
    

    return render(request, 'products/product_detail.html', {'product': product})

# Seller profile page with their products
@login_required(login_url='users:login')
def seller_profile_view(request, seller_id):
    seller_profile = get_object_or_404(SellerProfile, id=seller_id)

    products = ProductListings.objects.filter(seller=seller_profile)

    return render(request, 'products/seller_profile.html', {
        'products':products,
        'seller': seller_profile
        
        
        })