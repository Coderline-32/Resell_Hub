from django.shortcuts import render, redirect, get_object_or_404
from.forms import ProductListingForm
from django.contrib.auth.decorators import login_required
from users.models import SellerProfile
from .models import ProductListings
from .permissions import IsSellerOrReadOnly
from .serializers import ProductsSerializer, CategorySerializer, MyProductsSerializer
from rest_framework import generics, filters, permissions

# Create your views here.
class ProductsListView(generics.ListAPIView):
    queryset = ProductListings.objects.all().order_by("-created_at")
    serializer_class = ProductsSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description', 'category_name']
    ordering_fields = ['category__name', 'price', 'location', 'created_at' ]

    

    def perform_create(self, serializer):
        try:
            seller_profile = self.request.user.seller_profile
        except SellerProfile.DoesNotExist:
            raise PermissionError("You must be a seller to create products")
        
        serializer.save(seller=seller_profile)


class ProductDetailView(generics.RetrieveAPIView):
    """
    GET: View a product (anyone can view)
    PUT/PATCH/DELETE: Only owner (seller) can update or delete
    
    """
    queryset = ProductListings.objects.all()
    serializer_class = ProductsSerializer
    
class MyProductsView(generics.ListCreateAPIView):
    serializer_class = MyProductsSerializer
    permission_classes = [IsSellerOrReadOnly]

    def get_queryset(self):
        seller_data = ProductListings.objects.filter(seller=self.request.user.seller_profile)
        return seller_data
    def perform_create(self, serializer):
        return serializer.save(seller=self.request.user.seller_profile)

class MyProductsDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MyProductsSerializer
    permission_classes = [IsSellerOrReadOnly] 

    def get_queryset(self):
        product_detail = ProductListings.objects.filter(seller=self.request.user.seller_profile)
        return product_detail
    
    
        


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

@login_required
def seller_dashboard(request):
    try:
        seller_profile = request.user.seller_profile
    
    except SellerProfile.DoesNotExist:
        return redirect('products:home')
    
    products = ProductListings.objects.filter(posted_by=seller_profile)

    return render(request, 'products/seller_dashboard.html', {'products': products})


@login_required
def delete_product(request, product_id):
    try:
        seller_profile = request.user.seller_profile

    except SellerProfile.DoesNotExist:
        return redirect('products:home')
    
    del_product = get_object_or_404(ProductListings, id= product_id, posted_by = seller_profile)
    
    if request.method == 'POST':
            del_product.delete()
            return redirect('products:seller_dashboard')
    
@login_required(login_url = 'index') #Ensures only logged inusers can access the page
def home_view(request):

    products = ProductListings.objects.all()
    return render(request,  'products/home.html', {'products': products})