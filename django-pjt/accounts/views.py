from django.shortcuts import render

# Create your views here.
from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    # 요청에서 username과 password 가져오기
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        # JWT 토큰 생성
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)
        return Response({
            'access': access_token,
            'refresh': refresh_token,
            'user': {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            },
        })

@api_view(['POST'])
@permission_classes([AllowAny])
def social_login(request):
    email = request.data.get('email')
    print(email)
    try:
        user = User.objects.get(email=email)
        print(user)
    except User.DoesNotExist:
        return Response({
            'message': '가입되지 않은 사용자입니다.'
        }, status.HTTP_400_BAD_REQUEST)

    # JWT 토큰 발급
    refresh = RefreshToken.for_user(user)
    return Response({
        'access': str(refresh.access_token),
        'refresh': str(refresh),
    })

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def signup_products(request):
    user = request.user
    product_id = request.data.get('product_id')
    option_id = request.data.get('option_id')

    if not isinstance(user.registered_ptcd, list):
            user.registered_ptcd = []  # 초기화

    if (product_id, option_id) not in user.registered_ptcd:  # 중복 방지
        user.registered_ptcd.append((product_id, option_id))

    user.save()  # 변경사항 저장
    return Response({
        "message": "상품 가입이 완료되었습니다.",
        "registered_ptcd": user.registered_ptcd
    }, status=status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([AllowAny])
def id_check(request):
    username = request.data.get('username')
    print('username', username)
    if User.objects.filter(username=username).exists():
        return Response({"message":"이미 존재하는 ID"}, status.HTTP_400_BAD_REQUEST)
    return Response({"message":"사용 가능한 ID"}, status.HTTP_200_OK)