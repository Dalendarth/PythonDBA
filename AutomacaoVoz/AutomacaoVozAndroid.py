import androidhelper
import time

droid = androidhelper.Android()

def lock_screen():
    dpm = droid.getDevicePolicyManager()
    if dpm.isAdminActive():
        dpm.lockNow()
    else:
        print("Permissão de administrador não concedida.")

def unlock_screen():
    dpm = droid.getDevicePolicyManager()
    if dpm.isAdminActive():
        dpm.resetPassword("", 0)
        dpm.lockNow()
    else:
        print("Permissão de administrador não concedida.")

def open_app(app_name):
    pm = droid.getPackageManager()
    apps = pm.queryIntentActivities(pm.getLaunchIntentForPackage(app_name), 0)
    if apps:
        app = apps[0]
        app_package = app['activityInfo']['applicationInfo']['packageName']
        app_intent = pm.getLaunchIntentForPackage(app_package)
        droid.startActivity(app_intent)
    else:
        print(f"Não foi possível encontrar o aplicativo {app_name}.")

while True:
    print("Aguardando comando de voz...")
    result = droid.recognizeSpeech()
    if result and result['status'] == 'success':
        text = result['result'][0].lower()
        if 'travar' in text:
            lock_screen()
            print("Tela travada.")
        elif 'destravar' in text:
            unlock_screen()
            print("Tela destravada.")
        elif 'abrir' in text:
            app_name = text.replace('abrir ', '')
            open_app(app_name)
            print(f"Abrindo o aplicativo {app_name}.")
        else:
            print("Comando não reconhecido.")
    time.sleep(1)
