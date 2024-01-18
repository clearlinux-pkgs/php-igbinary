#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: phpize
# autospec version: v3
# autospec commit: c1050fe
#
Name     : php-igbinary
Version  : 3.2.15
Release  : 72
URL      : https://pecl.php.net/get/igbinary-3.2.15.tgz
Source0  : https://pecl.php.net/get/igbinary-3.2.15.tgz
Summary  : PHP igbinary extension
Group    : Development/Tools
License  : BSD-3-Clause
Requires: php-igbinary-lib = %{version}-%{release}
Requires: php-igbinary-license = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : perl(Getopt::Long)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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

%description dev
dev components for the php-igbinary package.


%package lib
Summary: lib components for the php-igbinary package.
Group: Libraries
Requires: php-igbinary-license = %{version}-%{release}

%description lib
lib components for the php-igbinary package.


%package license
Summary: license components for the php-igbinary package.
Group: Default

%description license
license components for the php-igbinary package.


%prep
%setup -q -n igbinary-3.2.15
cd %{_builddir}/igbinary-3.2.15
pushd ..
cp -a igbinary-3.2.15 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-igbinary
cp %{_builddir}/igbinary-%{version}/COPYING %{buildroot}/usr/share/package-licenses/php-igbinary/3fb06c4906ee841b51af78140d85d0e3b523d074 || :
%make_install

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/extensions/no-debug-non-zts-20230831/igbinary.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-igbinary/3fb06c4906ee841b51af78140d85d0e3b523d074
