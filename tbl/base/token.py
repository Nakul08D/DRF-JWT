from rest_framework_simplejwt.tokens import RefreshToken

def generate_jwt_token(user):
    """
    Generates JWT access and refresh tokens for a given user.

    Args:
        user: The user object for which tokens are to be generated.

    Returns:
        dict: A dictionary containing access and refresh tokens.
    """
    # Generate the refresh token
    refresh = RefreshToken.for_user(user)
    
    # Generate the access token from the refresh token
    access_token = str(refresh.access_token)
    
    # Return both the access and refresh tokens
    return {
        'access': access_token,
        'refresh': str(refresh),
    }
