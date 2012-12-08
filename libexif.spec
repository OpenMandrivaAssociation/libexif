%define major		12
%define libname		%mklibname exif %{major}
%define develname	%mklibname exif -d
%define langname	libexif-%{major}

Summary:	Library to access EXIF files (extended JPEG files)
Name:		libexif
Version:	0.6.21
Release:	2
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

%package -n %{develname}
Summary: 	Headers and links to compile against the "%{libname}" library
Group:		Development/C
Requires: 	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains all files which one needs to compile programs using
the "%{libname}" library.

%prep
%setup -q
%patch0 -p2 -b .includedir

%build
#sh ./autogen.sh
libtoolize --copy --force; aclocal -I auto-m4 -I m4m; autoconf; automake

%configure2_5x --disable-static
%make

%install
%makeinstall

%find_lang %{langname}

%files -n %{name}%{major}-common -f %{langname}.lang

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_docdir}/libexif


%changelog
* Fri Jul 13 2012 Oden Eriksson <oeriksson@mandriva.com> 0.6.21-1
+ Revision: 809121
- 0.6.21
- various fixes

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6.20-2
+ Revision: 661459
- mass rebuild

* Thu Dec 16 2010 Funda Wang <fwang@mandriva.org> 0.6.20-1mdv2011.0
+ Revision: 622368
- update to new version 0.6.20

* Thu Nov 25 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.19-2mdv2011.0
+ Revision: 601044
- rebuild

* Fri Nov 13 2009 Frederik Himpe <fhimpe@mandriva.org> 0.6.19-1mdv2010.1
+ Revision: 465749
- update to new version 0.6.19

* Sat Nov 07 2009 Frederik Himpe <fhimpe@mandriva.org> 0.6.18-1mdv2010.1
+ Revision: 462739
- Update to new version 0.6.18

* Sun Oct 04 2009 Frederik Himpe <fhimpe@mandriva.org> 0.6.17-6mdv2010.0
+ Revision: 453718
- Rebuild for missing packages

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.6.17-5mdv2010.0
+ Revision: 425538
- rebuild

* Wed Apr 08 2009 Pascal Terjan <pterjan@mandriva.org> 0.6.17-4mdv2009.1
+ Revision: 365187
- Add missing conflict for upgrade from 2009.0

* Sun Nov 30 2008 Frederik Himpe <fhimpe@mandriva.org> 0.6.17-3mdv2009.1
+ Revision: 308453
- Protect major in file list
- Fix license
- Move i18n files to libexif12-common: the mo file names contain the
  library's major. Add necessary obsoletes, conflicts and requires tags
  in order to make upgrades work correctly
- Prevent duplicate installation of doc files

* Sat Nov 29 2008 Frederik Himpe <fhimpe@mandriva.org> 0.6.17-2mdv2009.1
+ Revision: 307969
- Create binary libexif package containing translations (bug #35369)
- Remove now unneeded perl hack in SPEC file (thanks to Dan Fandrich)

* Wed Nov 19 2008 Frederik Himpe <fhimpe@mandriva.org> 0.6.17-1mdv2009.1
+ Revision: 304462
- New version 0.6.17
- Remove 2 patches for CVE fixed upstream

* Sat Jun 28 2008 Oden Eriksson <oeriksson@mandriva.com> 0.6.16-6mdv2009.0
+ Revision: 229910
- fix build

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - fix spacing at top of description

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Jan 25 2008 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.6.16-4mdv2008.1
+ Revision: 157942
- Added patches for CVE-2007-6351 and CVE-2007-6352. Closes: #36620

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 0.6.16-3mdv2008.1
+ Revision: 150557
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Jul 31 2007 Adam Williamson <awilliamson@mandriva.org> 0.6.16-2mdv2008.0
+ Revision: 57206
- fix files - move all non-library files to the -devel package (#31077)
- new devel policy
- specify license LGPLv2.1
- spec clean

* Thu Jun 21 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.6.16-1mdv2008.0
+ Revision: 42327
- New upstream: 0.6.16

* Wed May 16 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.6.14-1mdv2008.0
+ Revision: 27432
- New upstream: 0.6.14
- Use -p switch for post scripts that only runs ldconfig
- Specfile cleanup
- Improved i18n handling.

