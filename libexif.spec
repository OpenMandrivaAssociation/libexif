%define name	libexif
%define version	0.6.16
%define release	%mkrel 4

%define libname		%mklibname exif 12
%define develname	%mklibname exif -d
%define langname	libexif-12

Summary:	Library to access EXIF files (extended JPEG files)
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	LGPLv2.1
Group:		Graphics
Url:		http://sourceforge.net/projects/libexif/
Source:		http://belnet.dl.sourceforge.net/sourceforge/libexif/libexif-%{version}.tar.bz2
Patch0:		libexif-0.6.13-pkgconfig-fix.patch
Patch1:		CVE-2007-6351.patch
Patch2:		CVE-2007-6352.patch
Provides:	libexif
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	doxygen

%description
Most digital cameras produce EXIF files, which are JPEG files with
extra tags that contain information about the image. The EXIF library
allows you to parse an EXIF file and read the data from those tags.

%package -n %{libname}
Summary:	Library to access EXIF files (extended JPEG files)
Provides:	libexif
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
%patch1 -p1
%patch2 -p1

# Fix broken libexif/exif-utils.c
perl -p -i -e 's:^(\s*)static\s*(ExifSShort):$1$2:' libexif/exif-utils.c

##### BUILD #####

%build
autoconf

%configure2_5x
%make

##### INSTALL #####

%install
rm -rf %buildroot
%makeinstall
%find_lang %{langname}

##### PRE/POST INSTALL SCRIPTS #####

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf %buildroot

##### FILE LISTS FOR ALL BINARY PACKAGES #####

##### libexif
%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.*

##### libexif-devel
%files -n %{develname} -f %{langname}.lang
%defattr(-,root,root)
%doc ABOUT-NLS COPYING ChangeLog README
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_docdir}/libexif
