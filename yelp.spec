# TODO:
# move stylesheets to /usr/share/sgml
# use more generic stylesheet location
# remove docbook dtds and stylesheets from package and use system xml catalog
Summary:	A system documentation reader from the Gnome project
Summary(pl):	Czytnik dokumentacji z projektu GNOME
Name:		yelp
Version:	2.3.3
Release:	1
License:	GPL
Group:		X11/Applications
# Source0-md5:	235b7104217f21c7568269201336e346
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.3/%{name}-%{version}.tar.bz2
Patch0:		%{name}-pixmapsdir.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.1.90
BuildRequires:	ORBit2-devel >= 2.6.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	glib2-devel >= 2.2.0
BuildRequires:	gnome-vfs2-devel >= 2.2.0
BuildRequires:	libgnome-devel >= 2.1.90
BuildRequires:	libgnomeui-devel >= 2.1.90
BuildRequires:	libgtkhtml-devel >= 2.2.0
BuildRequires:	libxslt-devel >= 1.0.24
BuildRequires:	pkgconfig >= 0.12.0
BuildRequires:	rpm-build >= 4.1-10
Requires(post):	GConf2
Requires:	docbook-style-xsl >= 1.55.0
Requires:	gnome-vfs2 >= 2.2.0
Requires:	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Yelp is the Gnome 2 help/documentation browser. It is designed to help
you browse all the documentation on your system in one central tool.

%description -l pl
Yelp jest przegl±dark± pomocy i dokumentacji GNOME 2. Ma pomagaæ w
przegl±daniu ca³ej dokumentacji systemu w jednym, centralnym
narzêdziu.

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
install -d $RPM_BUILD_ROOT

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
%{_datadir}/sgml/docbook/%{name}
%{_pixmapsdir}/%{name}
%{_desktopdir}/*
