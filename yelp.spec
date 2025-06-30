Summary:	A system documentation reader from the GNOME project
Summary(pl.UTF-8):	Czytnik dokumentacji z projektu GNOME
Name:		yelp
Version:	42.3
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/yelp/42/%{name}-%{version}.tar.xz
# Source0-md5:	55f5edc7e1d52797a8fba23540fa72c1
URL:		https://wiki.gnome.org/Apps/Yelp
BuildRequires:	bzip2-devel
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.67.4
BuildRequires:	gtk+3-devel >= 3.13.3
BuildRequires:	gtk-doc-automake >= 1.13
BuildRequires:	gtk-webkit4.1-devel >= 2.36.0
BuildRequires:	itstool >= 1.2.0
BuildRequires:	libhandy1-devel >= 1.5.0
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	libxslt-devel >= 1.1.22
BuildRequires:	meson >= 1.3
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig >= 1:0.15.0
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	xz-devel >= 1:4.9
BuildRequires:	yelp-xsl >= 42.3
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.67.4
Requires:	%{name}-libs = %{version}-%{release}
Requires:	docbook-dtd412-xml
Requires:	docbook-dtd42-xml
Requires:	docbook-dtd43-xml
Requires:	docbook-dtd44-xml
Requires:	docbook-dtd45-xml
Requires:	docbook-style-xsl-nons >= 1.55.0
Requires:	yelp-xsl >= 42.3
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
Requires:	glib2 >= 1:2.67.4
Requires:	gtk+3 >= 3.13.3
Requires:	libhandy1 >= 1.5.0
Requires:	libxml2 >= 1:2.6.31
Requires:	libxslt >= 1.1.22
Obsoletes:	yelp-apidocs < 42

%description libs
yelp library.

%description libs -l pl.UTF-8
Biblioteka yelp.

%package devel
Summary:	Header files for yelp library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki yelp
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.67.4
Requires:	gtk+3-devel >= 3.13.3
Requires:	gtk-webkit4.1-devel >= 2.36.0
Requires:	libxml2-devel >= 1:2.6.31
Requires:	libxslt-devel >= 1.1.22

%description devel
Header files for yelp library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki yelp.

%prep
%setup -q

%build
%meson \
	--default-library=shared \
	-Dbzip2=enabled \
	-Dlzma=enabled

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

# not supported by glibc (as of 2.41)
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%glib_compile_schemas

%postun
%update_desktop_database_postun
%glib_compile_schemas

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md TODO
%attr(755,root,root) %{_bindir}/gnome-help
%attr(755,root,root) %{_bindir}/yelp
%{_datadir}/glib-2.0/schemas/org.gnome.yelp.gschema.xml
%{_datadir}/metainfo/yelp.appdata.xml
%{_datadir}/yelp
%{_datadir}/yelp-xsl/xslt/common/domains/yelp.xml
%{_desktopdir}/yelp.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Yelp.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Yelp-symbolic.svg

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libyelp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libyelp.so.0
%dir %{_libdir}/yelp
%dir %{_libdir}/yelp/web-extensions
%attr(755,root,root) %{_libdir}/yelp/web-extensions/libyelpwebextension.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libyelp.so
%{_includedir}/libyelp
