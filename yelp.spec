Summary:	A system documentation reader from the GNOME project
Summary(pl.UTF-8):	Czytnik dokumentacji z projektu GNOME
Name:		yelp
Version:	3.0.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/yelp/3.0/%{name}-%{version}.tar.bz2
# Source0-md5:	4ea6e6ae2fdff0d3768201e980a4ea27
URL:		http://projects.gnome.org/yelp/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	bzip2-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils >= 0.20.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	gtk-doc >= 1.13
BuildRequires:	gtk-webkit3-devel >= 1.3.2
BuildRequires:	intltool >= 0.41.0
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	libxslt-devel >= 1.1.22
BuildRequires:	lzma-devel
BuildRequires:	pkgconfig >= 1:0.15.0
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	sqlite3-devel
BuildRequires:	yelp-xsl >= 3.0.1
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.26.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name}-libs = %{version}-%{release}
Requires:	docbook-dtd412-xml
Requires:	docbook-dtd42-xml
Requires:	docbook-dtd43-xml
Requires:	docbook-dtd44-xml
Requires:	docbook-style-xsl >= 1.55.0
Requires:	gnome-doc-utils >= 0.20.0
Requires:	gnome-icon-theme-symbolic
Requires:	hicolor-icon-theme
Requires:	yelp-xsl >= 3.0.1
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Yelp is the default help browser for the GNOME desktop. Yelp provides
a simple graphical interface for viewing DocBook, HTML, man, and info
formatted documentation.

%description -l pl.UTF-8
Yelp jest domyślną przeglądarką pomocy dla biurka GNOME. Dostarcza
prosty graficzny interfejs do oglądania dokumentacji w formatach
DocBook, HTML, man i info.

%package libs
Summary:	yelp library
Summary(pl.UTF-8):	Biblioteka yelp
Group:		Libraries

%description libs
yelp library.

%description libs -l pl.UTF-8
Biblioteka yelp.

%package devel
Summary:	Header files for yelp library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki yelp
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.28.0
Requires:	gtk+3-devel >= 3.0.0
Requires:	gtk-webkit3-devel >= 1.3.2
Requires:	libxml2-devel >= 1:2.6.31
Requires:	libxslt-devel >= 1.1.22

%description devel
Header files for yelp library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki yelp.

%package apidocs
Summary:	yelp library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki yelp
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
yelp library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki yelp.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-schemas-compile \
	--disable-static \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_desktop_database_post
%glib_compile_schemas

%postun
%update_icon_cache hicolor
%update_desktop_database_postun
%glib_compile_schemas

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog NEWS TODO AUTHORS
%attr(755,root,root) %{_bindir}/gnome-help
%attr(755,root,root) %{_bindir}/yelp
%{_datadir}/glib-2.0/schemas/org.gnome.yelp.gschema.xml
%{_datadir}/yelp
%{_desktopdir}/yelp.desktop
%{_iconsdir}/hicolor/*/*/yelp-icon-big.png

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libyelp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libyelp.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libyelp.so
%{_includedir}/libyelp

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libyelp
