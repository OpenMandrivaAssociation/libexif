%define libname		%mklibname exif 12
%define develname	%mklibname exif -d
%define langname	libexif-12

Summary:	Library to access EXIF files (extended JPEG files)
Name:		libexif
Version:	0.6.17
Release:	%mkrel 2
License:	LGPLv2.1
Group:		Graphics
Url:		http://sourceforge.net/projects/libexif/
Source:		http://belnet.dl.sourceforge.net/sourceforge/libexif/libexif-%{version}.tar.bz2
Patch0:		libexif-0.6.13-pkgconfig-fix.patch
Provides:	libexif
BuildRequires:	doxygen
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Conflicts:	%{mklibname exif 12} < 0.6.17-2

%description
Most digital cameras produce EXIF files, which are JPEG files with
extra tags that contain information about the image. The EXIF library
allows you to parse an EXIF file and read the data from those tags.

%package -n %{libname}
Summary:	Library to access EXIF files (extended JPEG files)
Provides:	libexif
Requires:	%{name} = %{version}-%{release}
Group:		Graphics

%description -n %{libname}
Most digital cameras produce EXIF files, which are JPEG files with
extra tags that contain information about the image. The EXIF library
allows you to parse an EXIF file and read the data from those tags.

%package -n %{develname}
Summary: 	Headers and links to compile against the "%{libname}" library
Requires: 	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname exif 12 -d}
Group:		Development/C

%description -n %{develname}
This package contains all files which one needs to compile programs using
the "%{libname}" library.


##### PREP #####

%prep
%setup -q
%patch0 -p2 -b .includedir

##### BUILD #####

%build
#sh ./autogen.sh
libtoolize --copy --force; aclocal -I auto-m4 -I m4m; autoconf; automake

%configure2_5x
%make

##### INSTALL #####

%install
rm -rf %buildroot
%makeinstall
%find_lang %{langname}

##### PRE/POST INSTALL SCRIPTS #####

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %buildroot

##### FILE LISTS FOR ALL BINARY PACKAGES #####
%files -f %{langname}.lang
%doc AUTHORS README

##### libexif
%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.*

##### libexif-devel
%files -n %{develname} -f %{langname}.lang
%defattr(-,root,root)
%doc ABOUT-NLS ChangeLog
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_docdir}/libexif

