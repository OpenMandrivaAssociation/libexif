##### GENERAL STUFF #####

%define libname %mklibname exif 12

Summary:	Library to access EXIF files (extended JPEG files)
Name:		libexif
Version:	0.6.13
Release:	%mkrel 4
License:	LGPL
Group:		Graphics
Url:		http://sourceforge.net/projects/libexif/

##### SOURCE FILES #####

Source: http://belnet.dl.sourceforge.net/sourceforge/libexif/libexif-%{version}.tar.bz2
Patch0: libexif-0.6.13-pkgconfig-fix.patch

##### ADDITIONAL DEFINITIONS #####

Provides:	libexif
BuildRoot: %{_tmppath}/%{name}-buildroot

BuildRequires:	doxygen

##### SUB-PACKAGES #####

%description

Most digital cameras produce EXIF files, which are JPEG files with
extra tags that contain information about the image. The EXIF library
allows you to parse an EXIF file and read the data from those tags.

%package -n %libname
Summary:	Library to access EXIF files (extended JPEG files)
Provides:	libexif
Group:		Graphics

%description -n %libname

Most digital cameras produce EXIF files, which are JPEG files with
extra tags that contain information about the image. The EXIF library
allows you to parse an EXIF file and read the data from those tags.

%package -n %{libname}-devel
Summary: 	Headers and links to compile against the "%{libname}" library
Requires: 	%{libname} = %{version}
Provides:	libexif-devel
Group:		Development/C

%description -n %{libname}-devel
This package contains all files which one needs to compile programs using
the "%{libname}" library.


##### PREP #####

%prep
rm -rf $RPM_BUILD_DIR/libexif-%{version}
%setup -q -n libexif-%{version}
%patch0 -p1 -b .includedir

# Fix broken libexif/exif-utils.c
perl -p -i -e 's:^(\s*)static\s*(ExifSShort):$1$2:' libexif/exif-utils.c

##### BUILD #####

%build
# "autogen" is needed because we have a CVS snapshot.
#./autogen.sh

# Fix broken "./configure" script
#perl -p -i -e 's:^(AC_OUTPUT.*)$:$1 po/Makefile.in:' configure.in
autoconf-2.5x

%configure2_5x
%make

##### INSTALL #####

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

%find_lang %{name}

##### PRE/POST INSTALL SCRIPTS #####

%post -n %{libname} 

/sbin/ldconfig

%postun -n %{libname} 

/sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT


##### FILE LISTS FOR ALL BINARY PACKAGES #####

##### libexif
%files -n %libname -f %{name}.lang
%defattr(-,root,root)
%doc ABOUT-NLS COPYING ChangeLog README
%{_libdir}/*.so.*
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/*
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/*
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/*
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/*

##### libexif-devel
%files -n %{libname}-devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_docdir}/libexif

##### CHANGELOG #####


