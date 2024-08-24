import os
import base64

# Get environment variables
apk_sign_pwd = os.getenv('APK_SIGN_PWD')
apk_sign_jks = os.getenv('APK_SIGN_JKS')
apk_sign_alias = os.getenv('APK_SIGN_ALIAS')



# Ensure the directories exist
os.makedirs('android/app', exist_ok=True)

# Write the key.properties file
with open('android/key.properties', 'w') as f:
    f.write(f'keyPassword={apk_sign_pwd}\n')
    f.write(f'storePassword={apk_sign_pwd}\n')
    f.write(f'keyAlias={apk_sign_alias}\n')
    f.write('storeFile=key.jks\n')

# Decode the base64 encoded JKS and write to file
with open('android/app/key.jks', 'wb') as f:
    f.write(base64.b64decode(apk_sign_jks))
