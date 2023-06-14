#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-google_api_core
Version  : 2.11.1
Release  : 50
URL      : https://files.pythonhosted.org/packages/f3/b8/f727ada5b63aba53848e3791dd57be7481d5c9bf86978600ca9cca4ab03e/google-api-core-2.11.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/f3/b8/f727ada5b63aba53848e3791dd57be7481d5c9bf86978600ca9cca4ab03e/google-api-core-2.11.1.tar.gz
Summary  : Google API client core library
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-google_api_core-license = %{version}-%{release}
Requires: pypi-google_api_core-python = %{version}-%{release}
Requires: pypi-google_api_core-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(google_auth)
BuildRequires : pypi(googleapis_common_protos)
BuildRequires : pypi(protobuf)
BuildRequires : pypi(requests)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Core Library for Google Client Libraries
========================================

%package license
Summary: license components for the pypi-google_api_core package.
Group: Default

%description license
license components for the pypi-google_api_core package.


%package python
Summary: python components for the pypi-google_api_core package.
Group: Default
Requires: pypi-google_api_core-python3 = %{version}-%{release}

%description python
python components for the pypi-google_api_core package.


%package python3
Summary: python3 components for the pypi-google_api_core package.
Group: Default
Requires: python3-core
Provides: pypi(google_api_core)
Requires: pypi(google_auth)
Requires: pypi(googleapis_common_protos)
Requires: pypi(protobuf)
Requires: pypi(requests)

%description python3
python3 components for the pypi-google_api_core package.


%prep
%setup -q -n google-api-core-2.11.1
cd %{_builddir}/google-api-core-2.11.1
pushd ..
cp -a google-api-core-2.11.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1686785536
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . protobuf
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . protobuf
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-google_api_core
cp %{_builddir}/google-api-core-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-google_api_core/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
python3 -tt setup.py build  install --root=%{buildroot}
pypi-dep-fix.py %{buildroot} protobuf
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-google_api_core/2b8b815229aa8a61e483fb4ba0588b8b6c491890

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
