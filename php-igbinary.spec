#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-igbinary
Version  : 3.1.1
Release  : 3
URL      : https://pecl.php.net/get/igbinary-3.1.1.tgz
Source0  : https://pecl.php.net/get/igbinary-3.1.1.tgz
Summary  : A drop in replacement for the standard php serializer
Group    : Development/Tools
License  : BSD-3-Clause
Requires: php-igbinary-lib = %{version}-%{release}
BuildRequires : buildreq-php

%description
Igbinary is a drop in replacement for the standard PHP serializer. 
Instead of time and space consuming textual representation, 
igbinary stores PHP data structures in a compact binary form.

%package dev
Summary: dev components for the php-igbinary package.
Group: Development
Requires: php-igbinary-lib = %{version}-%{release}
Provides: php-igbinary-devel = %{version}-%{release}
Requires: php-igbinary = %{version}-%{release}
Requires: php-igbinary = %{version}-%{release}

%description dev
dev components for the php-igbinary package.


%package lib
Summary: lib components for the php-igbinary package.
Group: Libraries

%description lib
lib components for the php-igbinary package.


%prep
%setup -q -n igbinary-3.1.1
cd %{_builddir}/igbinary-3.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/php/ext/igbinary/igbinary.h
/usr/include/php/ext/igbinary/php_igbinary.h
/usr/include/php/ext/igbinary/src/php7/igbinary.h
/usr/include/php/ext/igbinary/src/php7/php_igbinary.h

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20180731/igbinary.so
