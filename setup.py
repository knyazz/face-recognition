[metadata]
name = python-face-recognition-wrapper
version = 0.1.0
author = Smirnov.EV
author_email = knyazz@gmail.com
description = wrapper of face recognition sdk to compare faces
long_description = file: README.md
long_description_content_type = text/markdown
url = https://github.com/knyazz/face-recognition
classifiers =
    Programming Language :: Python
    License :: OSI Approved :: MIT License
    Operating System :: OS Independent
    Topic :: Software Development :: Libraries :: Python Modules
    Intended Audience :: Developers
    Development Status :: 4 - Beta

[options]

install_requires =
    numpy==1.21.3
    Pillow==8.4.0
    face_recognition_models==0.3.0
    dlib==19.22.1
    click==8.0.3
package_dir =
    = src
packages = find:
python_requires = >=3.6

[options.packages.find]
where = src