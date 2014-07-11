%define major	12
%define libname	%mklibname exif %{major}
%define devname	%mklibname exif -d
%define langname libexif-%{major}

Summary:	Library to access EXIF files (extended JPEG files)
Name:		libexif
Version:	0.6.21
Release:	13
License:	LGPLv2+
Group:		Graphics
Url:		http://sourceforge.net/projects/libexif/
Source0:	http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.bz2
Patch0:		libexif-0.6.13-pkgconfig-fix.patch
BuildRequires:	doxygen
BuildRequires:	libtool
BuildRequires:	gettext-devel

%description
Most digital cameras produce EXIF files, which are JPEG files with
extra tags that contain information about the image. The EXIF library
allows you to parse an EXIF file and read the data from those tags.

%package -n	%{name}%{major}-common
Summary:	Library to access EXIF files - Translations
Group:		Graphics

%description -n	%{name}%{major}-common
This package contains the translations for %{name}%{major}.

%package -n	%{libname}
Summary:	Library to access EXIF files (extended JPEG files)
Group:		System/Libraries
Provides:	libexif = %{version}-%{release}
Requires:	%{name}%{major}-common = %{version}-%{release}

%description -n	%{libname}
Most digital cameras produce EXIF files, which are JPEG files with
extra tags that contain information about the image. The EXIF library
allows you to parse an EXIF file and read the data from those tags.

%package -n	%{devname}
Summary:	Headers and links to compile against the "%{libname}" library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package contains all files which one needs to compile programs using
the "%{libname}" library.

%prep
%setup -q
%patch0 -p2 -b .includedir
autoreconf -fi -Iauto-m4 -Im4m

%build
%configure2_5x --disable-static
%make

%install
%makeinstall

%find_lang %{langname}

%files -n %{name}%{major}-common -f %{langname}.lang

%files -n %{libname}
%{_libdir}/libexif.so.%{major}*

%files -n %{devname}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_docdir}/libexif

