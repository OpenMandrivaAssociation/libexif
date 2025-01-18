# libgphoto uses libexif, wine uses libgphoto
%ifarch %{x86_64}
%bcond_without compat32
%endif

%define major 12
%define libname %mklibname exif %{major}
%define devname %mklibname exif -d
%define lib32name %mklib32name exif %{major}
%define dev32name %mklib32name exif -d
%define langname libexif-%{major}

Summary:	Library to access EXIF files (extended JPEG files)
Name:		libexif
Version:	0.6.25
Release:	1
License:	LGPLv2+
Group:		Graphics
Url:		https://sourceforge.net/projects/libexif/
Source0:	https://github.com/libexif/libexif/releases/download/v%{version}/libexif-%{version}.tar.bz2
Patch0:		libexif-0.6.13-pkgconfig-fix.patch
BuildRequires:	doxygen
BuildRequires:	libtool
BuildRequires:	gettext-devel
%if %{with compat32}
BuildRequires:	devel(libltdl)
BuildRequires:	devel(libasprintf)
%endif

%description
Most digital cameras produce EXIF files, which are JPEG files with
extra tags that contain information about the image. The EXIF library
allows you to parse an EXIF file and read the data from those tags.

%package -n %{name}%{major}-common
Summary:	Library to access EXIF files - Translations
Group:		Graphics

%description -n %{name}%{major}-common
This package contains the translations for %{name}%{major}.

%package -n %{libname}
Summary:	Library to access EXIF files (extended JPEG files)
Group:		System/Libraries
Provides:	libexif = %{version}-%{release}
Requires:	%{name}%{major}-common = %{version}-%{release}

%description -n %{libname}
Most digital cameras produce EXIF files, which are JPEG files with
extra tags that contain information about the image. The EXIF library
allows you to parse an EXIF file and read the data from those tags.

%package -n %{devname}
Summary:	Headers and links to compile against the "%{libname}" library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains all files which one needs to compile programs using
the "%{libname}" library.

%if %{with compat32}
%package -n %{lib32name}
Summary:	Library to access EXIF files (extended JPEG files) (32-bit)
Group:		System/Libraries

%description -n %{lib32name}
Most digital cameras produce EXIF files, which are JPEG files with
extra tags that contain information about the image. The EXIF library
allows you to parse an EXIF file and read the data from those tags.

%package -n %{dev32name}
Summary:	Headers and links to compile against the "%{libname}" library (32-bit)
Group:		Development/C
Requires:	%{devname} = %{version}-%{release}
Requires:	%{lib32name} = %{version}-%{release}

%description -n %{dev32name}
This package contains all files which one needs to compile programs using
the "%{lib32name}" library.
%endif

%prep
%setup -q
%patch 0 -p2 -b .includedir
autoreconf -fi -Iauto-m4 -Im4m

export CONFIGURE_TOP="$(pwd)"

%if %{with compat32}
mkdir build32
cd build32
%configure32
cd ..
%endif

mkdir build
cd build
%configure --disable-static

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build

%find_lang %{langname}

%files -n %{name}%{major}-common -f %{langname}.lang

%files -n %{libname}
%{_libdir}/libexif.so.%{major}*

%files -n %{devname}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_docdir}/libexif

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libexif.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/*.so
%{_prefix}/lib/pkgconfig/*
%endif
