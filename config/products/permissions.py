from rest_framework import permissions

class IsSellerOrReadOnly(permissions.BasePermission):
    """
    Allow everyone to view products (GET)
    Allow only sellers to create products (POST)
    Allow product owner only to update/delete the product
    """

    def has_permission(self, request, view):
        # Safe methods are allowed for everyone
        if request.method in permissions.SAFE_METHODS:
            return True
        # POST allowed only if user has a seller profile
        if request.method == 'POST':
            return hasattr(request.user, 'seller_profile')
        # Other methods require object-level check
        return True

    def has_object_permission(self, request, view, obj):
        # Safe methods are allowed for everyone
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only the product owner can update/delete
        return obj.seller == request.user.seller_profile
