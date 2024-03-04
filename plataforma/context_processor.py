def user_data(request):

    user = request.user
    if user.is_authenticated:
        user_data_processor = {
            'nickname': user.user_profile.nickname,  
        }
    else:
        user_data_processor = {}
    
    return {'user_data_processor': user_data_processor}