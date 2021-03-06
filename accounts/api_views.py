from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework import status
from random import randint
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from django.http import JsonResponse


from .serializers import *

# -------------------------------------------------------------------------------------------------------------------------------
"""
api's in api_views.py :

1-change_password --> change user password
2-user_create  --> create one account with phoneNumber
3-code_get --> get code for Account validation
4-user_update --> fill other information the user
5-user_get --> get info user



"""
# -------------------------------------------------------------------------------------------------------------------------------
@api_view(['POST'])
@permission_classes([AllowAny])
def user_create(request):
    info = UserSerializersValid(data=request.data)
    code = randint(1000, 9999)

    if info.is_valid():
        User(phoneNumber=info.validated_data['phoneNumber'],
             is_active=False,
             code=code).save()
        # send Code to User
        # temp = Sms_link.replace("phoneNumber",info.validated_data['phoneNumber'])
        # temp = temp.replace("code",str(code))
        # response = requests.get(temp)
        return Response({'message': 'ok', 'code': f'{code}'}, status=status.HTTP_201_CREATED)
    else:
        return Response(info.errors, status=status.HTTP_400_BAD_REQUEST)
# -------------------------------------------------------------------------------------------------------------------------------
@api_view(['POST'])
@permission_classes([AllowAny])
def user_update(request, phoneNumber):
    try:
        user = User.objects.get(phoneNumber=phoneNumber)
    except User.DoesNotExist:
        return Response({'error': 'this user does not exist'}, status=status.HTTP_404_NOT_FOUND)
    # info = UserSerializersUpdate(user, data=request.data)
    info = UserSerializersUpdate(data=request.data)

    if info.is_valid():
        user.firstName = info.validated_data['firstName']
        user.lastName = info.validated_data['lastName']
        user.is_active = True
        user.set_password(info.validated_data['password'])

        # cart = Cart(user=user)
        # cart.save()
        # user.cart = cart
        # department = Department(user=user)
        # department.save()
        # user.department = department

        user.save()

        return Response({'message': 'ok is updated'}, status=status.HTTP_200_OK)
    else:
        return Response(info.errors, status=status.HTTP_400_BAD_REQUEST)
# # -------------------------------------------------------------------------------------------------------------------------------
# @api_view(['POST'])
# @permission_classes([AllowAny])
# def change_password(request, phoneNumber):
#     info = ChangePasswordSerializersValid(data=request.data)
#     try:
#         user = User.objects.get(phoneNumber=phoneNumber)
#     except User.DoesNotExist:
#         return Response({'error': 'this user does not exist'}, status=status.HTTP_404_NOT_FOUND)
#
#     if info.is_valid():
#         if user.check_password(info.validated_data['old_password']):
#             user.set_password(info.validated_data['password'])
#             VALIDATION_CODE_FRONT = info.validated_data['VALIDATION_CODE']
#             if VALIDATION_CODE_FRONT == VALIDATION_CODE:
#                 user.save()
#                 return Response({'message': 'ok is updated'}, status=status.HTTP_200_OK)
#     else:
#         return Response(info.errors, status=status.HTTP_400_BAD_REQUEST)
#
# # -------------------------------------------------------------------------------------------------------------------------------
# @api_view(['POST'])
# @permission_classes([AllowAny])
# def change_password_without_old(request, phoneNumber):
#     info = ChangePasswordSerializersValid(data=request.data)
#     try:
#         user = User.objects.get(phoneNumber=phoneNumber)
#     except User.DoesNotExist:
#         return Response({'error': 'this user does not exist'}, status=status.HTTP_404_NOT_FOUND)
#
#     if info.is_valid():
#         user.set_password(info.validated_data['password'])
#         VALIDATION_CODE_FRONT = info.validated_data['VALIDATION_CODE']
#         if VALIDATION_CODE_FRONT == VALIDATION_CODE:
#             user.save()
#             return Response({'message': 'ok is updated'}, status=status.HTTP_200_OK)
#     else:
#         return Response(info.errors, status=status.HTTP_400_BAD_REQUEST)
#
# # -------------------------------------------------------------------------------------------------------------------------------
# @api_view(['POST'])
# @permission_classes([AllowAny])
# def code_get(request, phoneNumber):
#     info = CodeAgainSerializersValid(data=request.data)
#     try:
#         user = User.objects.get(phoneNumber=phoneNumber)
#     except User.DoesNotExist:
#         return Response({'error': 'this user does not exist'}, status=status.HTTP_404_NOT_FOUND)
#
#     code = randint(1000, 9999)
#     if info.is_valid():
#         # send Code to User
#         user.code = code
#         user.save()
#         # temp = Sms_link.replace("phoneNumber",info.validated_data['phoneNumber'])
#         # temp = temp.replace("code",str(code))
#         # response = requests.get(temp)
#         return Response({'message': 'ok', 'code': f'{code}'}, status=status.HTTP_201_CREATED)
#     else:
#         return Response(info.errors, status=status.HTTP_400_BAD_REQUEST)
# # -------------------------------------------------------------------------------------------------------------------------------
# @api_view(['GET'])
# @permission_classes([AllowAny])
# def user_get(request, phoneNumber):
#     try:
#         user = User.objects.get(phoneNumber=phoneNumber)
#     except User.DoesNotExist:
#         return Response({'error': 'this user does not exist'}, status=status.HTTP_404_NOT_FOUND)
#     ser_data = UserSerializersInfo(user)
#     return Response(ser_data.data, status=status.HTTP_200_OK)
# # -------------------------------------------------------------------------------------------------------------------------------
