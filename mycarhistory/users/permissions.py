from rest_framework import permissions


class ResourseListMethodPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'PUT':
            return False
        return True


class CarOwnerPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class TreatmentOwnerPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.car.user == request.user
