%define	major		12
%define libname		%mklibname exif %{major}
%define develname	%mklibname exif -d
%define langname	libexif-%{major}

Summary:	Library to access EXIF files (extended JPEG files)
Name:		libexif
Version:	0.6.21
Release:	1
License:	LGPLv2+
Group:		Graphics
Url:		http://sourceforge.net/projects/libexif/
Source:		http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.bz2
Patch0:		libexif-0.6.13-pkgconfig-fix.patch
BuildRequires:	doxygen
BuildRequires:	gettext-devel
BuildRequires:	autoconf automake libtool

%description
Most digital cameras produce EXIF files, which are JPEG files with
extra tags that contain information about the image. The EXIF library
allows you to parse an EXIF file and read the data from those tags.

%package -n %{name}%{major}-common
Summary:        Library to access EXIF files - Translations
Group:		Graphics
Conflicts:      %{mklibname -d exif 12} < 0.6.17-3
Conflicts:      %{mklibname -d exif} < 0.6.17-3
Conflicts:	libexif < 0.6.17-3
Obsoletes:	libexif < 0.6.17-3

%description -n %{name}%{major}-common
This package contains the translations for %{name}%{major}.

%package -n %{libname}
Summary:	Library to access EXIF files (extended JPEG files)
Provides:	libexif = %{version}-%{release}
Requires:	%{name}%{major}-common = %{version}-%{release}
Group:		Graphics

%description -n %{libname}
Most digital cameras produce EXIF files, which are JPEG files with
extra tags that contain information about the image. The EXIF library
allows you to parse an EXIF file and read the data from those tags.

%package -n %{develname}
Summary: 	Headers and links to compile against the "%{libname}" library
Requires: 	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname exif 12 -d}
Provides:	%{mklibname exif 12 -d} = %{version}-%{release}
Group:		Development/C

%description -n %{develname}
This package contains all files which one needs to compile programs using
the "%{libname}" library.


%prep
%setup -q
%patch0 -p2 -b .includedir

%build
#sh ./autogen.sh
libtoolize --copy --force; aclocal -I auto-m4 -I m4m; autoconf; automake

%configure2_5x
%make

%install

%makeinstall

%find_lang %{langname}

rm -f %{buildroot}%{_libdir}/*.*a

%files -n %{name}%{major}-common -f %{langname}.lang

%files -n %{libname} 
%{_libdir}/*.so.%{major}*

%files -n %{develname} 
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_docdir}/libexif
