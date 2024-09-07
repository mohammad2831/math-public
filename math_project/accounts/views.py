from django.shortcuts import render,redirect

from django.views import View
import random
from utils import send_otp_code
from . models import OtpCode, User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from .serializers import UserRegisterSerializer, UserLoginSerializer, VerifyCodeSerializer, UserProfileSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from .permissions import IsProfileOwner



class UserProfileView(APIView):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [IsAuthenticated,IsProfileOwner]

    def get(self, request):
 
        user = User.objects.get(email=request.user.email)

        ser_data = UserProfileSerializer(user)
        return Response(ser_data.data, status=status.HTTP_200_OK)
    

    def put(self, request, *args, **kwargs):
        user = request.user
        serializer = UserProfileSerializer(user, data=request.data, partial=True) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserLoginView(APIView):
    def post(self, request):
        ser_data = UserLoginSerializer(data=request.data)
        

        if ser_data.is_valid():
           
            email = ser_data.validated_data['email']
            password = ser_data.validated_data['password']

           
            user = get_object_or_404(User, email=email)

           
            if user.check_password(password):
                token, created = Token.objects.get_or_create(user=user)
                print(token.key)

                return Response({'token': token.key, 'status': 202})
            else:
                return Response({'error': 'Invalid credentials'}, status=400)

        return Response(ser_data.errors, status=400)





class UserRegisterVerifyCodeView(APIView):

        
    def post(self, request):
        user_session=request.session['user_registration_info']
        code_instance = OtpCode.objects.get(phone_number=user_session['phone_number'])


        ser_data = VerifyCodeSerializer(data=request.data)
        if ser_data.is_valid():
            
            if int(ser_data.validated_data['code']) == code_instance.code:

              
                user = User.objects.create_user(
                    email=user_session['email'],
                    phone_number=user_session['phone_number'],
                    full_name=user_session['full_name'],
                    password=user_session['password']
                    )
                
                code_instance.delete()
                token = Token.objects.create(user=user)
                return Response({'token': token.key,'status':205} )
            
            else:
                return Response({'status':400} )
            
        return Response({'status':401} )

class UserRegisterView(APIView):
    def post(self, request):
        ser_data = UserRegisterSerializer(data=request.data)
       
        if ser_data.is_valid():
            random_code = random.randint(1000, 9999)
       #     send_otp_code(ser_data.validated_data['phone_number'], random_code)
            OtpCode.objects.create(phone_number = ser_data.validated_data['phone_number'], code=random_code)

            request.session['user_registration_info'] = {
                'email' : ser_data.validated_data['email'],
                'phone_number' : ser_data.validated_data['phone_number'],
                'full_name' : ser_data.validated_data['full_name'],
                'password' : ser_data.validated_data['password']
            }
             
            return Response({'code':random_code,'status':201} )
        
        return Response(ser_data.errors, status=400)




'''
class UserRegisterView(View):
    form_class = UserRegistrationForm
    def get(self, request):
        form = self.form_class
        return render(request, 'accounts/register.html', {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = random.randint(1000, 9999)
            send_otp_code(form.cleaned_data['phone'], random_code)
            OtpCode.objects.create(phone_number = form.cleaned_data['phone'], code=random_code)

            request.session['user_registration_info'] = {
                'email' : form.cleaned_data['email'],
                'phone_number' : form.cleaned_data['phone'],
                'full_name' : form.cleaned_data['full_name'],
                'password' : form.cleaned_data['password'],
            }
            messages.success(request, 'we send you a code ', 'success')
            return redirect('accounts:user_register_verify_code')
        return render(request,'accounts/register.html', {'form':form})

'''
'''
class UserRegisterVerifyCodeView(View):
    form_class = VerifyCodeForm
    def get(self, request):
        form = self.form_class
        return render(request, 'accounts/verify.html', {'form':form})
        
    def post(self, request):
        user_session=request.session['user_registration_info']
        code_instance = OtpCode.objects.get(phone_number=user_session['phone_number'])

        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['code'] == code_instance.code:
                User.objects.create_user(user_session['email'], user_session['phone_number'], 
                                        user_session['full_name'], user_session['password'])
                
                code_instance.delete()
                messages.success(request, 'you registered .' 'success')
                return redirect('web:home')
            
            else:
                messages.error(request, 'code is wrong', 'danger')
                return redirect('accounts:user_register_verify_code')
            
        return redirect('web:home')
'''    

class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'you logout succes ', 'success')
        return redirect('web:home')

'''

class UserLoginView(View):
    form_class= UserLoginForm

    def get(self, request):
        form = self.form_class
        return render(request, 'accounts/login.html', {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'you logged in succes ', 'success')
                return redirect('web:home')
            
            messages.error(request,'email or password is wrong', 'danger')

        return render(request,'accounts/login.html', {'form':form})


'''

        

