from rest_framework import permissions


# Only owner can access the resource

class CarOwnerPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class TreatmentOwnerPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.car.user == request.user
