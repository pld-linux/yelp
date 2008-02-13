Summary:	A system documentation reader from the GNOME project
Summary(pl.UTF-8):	Czytnik dokumentacji z projektu GNOME
Name:		yelp
Version:	2.20.0
Release:	9
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/yelp/2.20/%{name}-%{version}.tar.bz2
# Source0-md5:	8902618c343093b1c64ee6d647ec41ed
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-bs.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.20.0
BuildRequires:	ORBit2-devel >= 1:2.14.9
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	dbus-glib-devel >= 0.73
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gnome-doc-utils >= 0.12.0
BuildRequires:	gnome-vfs2-devel >= 2.20.0
BuildRequires:	libbeagle-devel >= 0.3.0
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libgnomeui-devel >= 2.20.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.30
BuildRequires:	libxslt-devel >= 1.1.22
BuildRequires:	pkgconfig >= 1:0.15.0
BuildRequires:	rarian-devel
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xulrunner-devel >= 1.8.0.4
BuildRequires:	zlib-devel
Requires(post,preun):	GConf2
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	docbook-style-xsl >= 1.55.0
Requires:	gnome-doc-utils >= 0.12.0
Requires:	gnome-vfs2 >= 2.20.0
Requires:	libgnomeui >= 2.20.0
Requires:	scrollkeeper
%requires_eq_to	xulrunner xulrunner-devel
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# can be provided by mozilla or mozilla-embedded
%define		_noautoreqdep	libgtkembedmoz.so libgtksuperwin.so libxpcom.so
# we have strict deps for it
%define		_noautoreq	libxpcom.so

%description
Yelp is the GNOME help/documentation browser. It is designed to help
you browse all the documentation on your system in one central tool.

%description -l pl.UTF-8
Yelp jest przeglądarką pomocy i dokumentacji GNOME. Umożliwia
przeglądanie całej dokumentacji systemu za pomocą jednego, centralnego
narzędzia.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# fix locale names
sed -i -e s#nds\@NFE#nds# po/LINGUAS
sed -i -e s#sr\@Latn#sr\@latin# po/LINGUAS
mv po/nds{\@NFE,}.po
mv po/sr\@{Latn,latin}.po

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make} -j1 \
	CFLAGS="%{rpmcflags} -DI_KNOW_RARIAN_0_8_IS_UNSTABLE"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install yelp.schemas
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall yelp.schemas

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog NEWS TODO AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/*/yelp-icon-big.png
%{_sysconfdir}/gconf/schemas/yelp.schemas
