# TODO:
# move stylesheets to /usr/share/sgml
# use more generic stylesheet location
# remove docbook dtds and stylesheets from package and use system xml catalog
Summary:	A system documentation reader from the Gnome project
Summary(pl):	Czytnik dokumentacji z projektu GNOME
Name:		yelp
Version:	1.0.7
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/1.0/%{name}-%{version}.tar.bz2
Patch0:		%{name}-pixmapsdir.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libgnomeui-devel
BuildRequires:	libgtkhtml-devel
BuildRequires:	libxslt-devel
BuildRequires:	pkgconfig
Requires(post):	GConf2
Requires:	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME2

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
%{__aclocal} -I %{_aclocaldir}/gnome2-macros
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post 
GCONF_CONFIG_SOURCE="`%{_bindir}/gconftool-2 --get-default-source`" %{_bindir}/gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/*.schemas > /dev/null

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog NEWS TODO AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}
%{_datadir}/applications/*
%{_libdir}/bonobo/servers/*
%attr(755,root,root) %{_libdir}/%{name}-db2html
%{_datadir}/sgml/docbook/%{name}
