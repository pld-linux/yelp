%define gtk2_version 1.3.13
%define gtkhtml2_version 1.99.2
%define gnome_vfs2_version 1.9.4.91
%define libgnomeui_version 1.110.0
%define libbonobo_version 1.110.0

Summary:	A system documentation reader from the Gnome project
Summary(pl):	Czytnik dokumentacji z projektu GNOME
Name:		yelp
Version:	0.2
Release:	2
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Source0:	ftp://ftp.gnome.org/pub/gnome/pre-gnome2/sources/yelp/%{name}-%{version}.tar.bz2
Requires:	scrollkeeper
Requires:	gtk+2 >= %{gtk2_version}
Requires:	gnome-vfs2 >= %{gnome_vfs2_version}
Requires:	gtkhtml2 >= %{gtkhtml2_version}
Requires:	libgnomeui >= %{libgnomeui_version}
Requires:	libbonobo >= %{libbonobo_version}
BuildRequires:	gtk+2-devel >= %{gtk2_version}
BuildRequires:	gnome-vfs2-devel >= %{gnome_vfs2_version}
BuildRequires:	gtkhtml2-devel >= %{gtkhtml2_version}
BuildRequires:	libgnomeui-devel >= %{libgnomeui_version}
BuildRequires:	libbonobo-devel >= %{libbonobo_version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Yelp is the Gnome 2 help/documentation browser. It is designed to help
you browse all the documentation on your system in one central tool.

%description -l pl
Yelp jest przegl±dark± pomocy i dokumentacji GNOME 2. Ma pomagaæ w
przegl±daniu ca³ej dokumentacji systemu w jednym, centralnym
narzêdziu.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/yelp
%{_libdir}/bonobo/servers/GNOME_Yelp.server
%{_datadir}/applications/yelp.desktop
%{_datadir}/yelp
