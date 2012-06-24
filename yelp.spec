# TODO:
# move stylesheets to /usr/share/sgml
# use more generic stylesheet location
# remove docbook dtds and stylesheets from package and use system xml catalog
Summary:	A system documentation reader from the GNOME project
Summary(pl):	Czytnik dokumentacji z projektu GNOME
Name:		yelp
Version:	2.3.6
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.3/%{name}-%{version}.tar.bz2
# Source0-md5:	aab67ada710389166f6df121bab57881
Patch0:		%{name}-pixmapsdir.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.1.90
BuildRequires:	ORBit2-devel >= 2.7.5-1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	glib2-devel >= 2.2.0
BuildRequires:	gnome-vfs2-devel >= 2.2.0
BuildRequires:	libgnome-devel >= 2.1.90
BuildRequires:	libgnomeui-devel >= 2.3.3.1-2
BuildRequires:	libgtkhtml-devel >= 2.2.0
BuildRequires:	libtool
BuildRequires:	libxslt-devel >= 1.0.24
BuildRequires:	pkgconfig >= 0.12.0
BuildRequires:	rpm-build >= 4.1-10
Requires(post):	GConf2
Requires:	docbook-style-xsl >= 1.55.0
Requires:	gnome-vfs2 >= 2.2.0
Requires:	gnome-mime-data
Requires:	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Yelp is the GNOME 2 help/documentation browser. It is designed to help
you browse all the documentation on your system in one central tool.

%description -l pl
Yelp jest przegl�dark� pomocy i dokumentacji GNOME 2. Ma pomaga� w
przegl�daniu ca�ej dokumentacji systemu w jednym, centralnym
narz�dziu.

%prep
%setup  -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I %{_aclocaldir}/gnome2-macros
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog NEWS TODO AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_libdir}/bonobo/servers/*
%attr(755,root,root) %{_libdir}/%{name}-db2html
%attr(755,root,root) %{_libdir}/%{name}-info2html
%attr(755,root,root) %{_libdir}/%{name}-man2html
%{_datadir}/sgml/docbook/%{name}
%{_pixmapsdir}/%{name}
%{_desktopdir}/*
