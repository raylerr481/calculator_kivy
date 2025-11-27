[app]
title = Calculator Kivy
package.name = calculator_kivy
package.domain = org.rayler
source.dir = .
source.include_exts = py,kv,png,jpg,ttf
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[android]
sdk = 24
ndk = 25b
android.api = 33
android.minapi = 21
android.ndk_api = 21
