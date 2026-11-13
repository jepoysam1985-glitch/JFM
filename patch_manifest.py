p = 'android/app/src/main/AndroidManifest.xml'
s = open(p, encoding='utf-8').read()
names = ['FOREGROUND_SERVICE', 'FOREGROUND_SERVICE_MEDIA_PLAYBACK', 'WAKE_LOCK', 'POST_NOTIFICATIONS']
perms = ''.join('    <uses-permission android:name="android.permission.' + n + '" />\n' for n in names)
svc = '        <service android:name=".AudioKeepAliveService" android:exported="false" android:foregroundServiceType="mediaPlayback" />\n'
s = s.replace('<application', perms + '\n    <application', 1)
s = s.replace('</application>', svc + '    </application>', 1)
open(p, 'w', encoding='utf-8').write(s)
print('Manifest patched')
