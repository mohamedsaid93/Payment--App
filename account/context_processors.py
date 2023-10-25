from account.models import KYC

def kyc_context_processor(request):
    #if request.user.is_authenticated:
    try:
        kycCP = KYC.objects.get(user=request.user)
        
    except:
        kycCP = None


    return {
            'kycCP':kycCP,
            }

