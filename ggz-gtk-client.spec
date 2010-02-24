Summary:	GTK+ version of GGZ client
Summary(pl.UTF-8):	Klient GGZ napisany z użyciem GTK+
Name:		ggz-gtk-client
Version:	0.0.14.1
Release:	3
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://ftp.belnet.be/packages/ggzgamingzone/ggz/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	87f67ff01f867bd04ba894a7c6a9f7fc
Source1:	%{name}.xpm
Patch0:		%{name}-desktop.patch
URL:		http://www.ggzgamingzone.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
# gaim plugin?
#BuildRequires:	gaim-devel >= 1.5.0
BuildRequires:	gettext-devel
BuildRequires:	ggz-client-libs-devel >= 0.0.14
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libggz-devel >= 0.0.14
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GGZ core clients enable players to access the GGZ server to chat, meet
other people in the game lobbies, play with them, watch their scores,
and be spectator other people's games. This is GTK+ version of GGZ
client.

%description -l pl.UTF-8
Programy klienckie GGZ umożliwiają graczom dostęp do serwerów GGZ z
możliwością rozmowy, poznawania innych ludzi w grze, granie z nimi,
obserwowanie punktacji oraz obserwowanie rozgrywek innych ludzi. Ten
klient GGZ to wersja napisana z użyciem GTK+.

%package devel
Summary:	Header files for ggz-gtk library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki ggz-gtk
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ggz-client-libs-devel >= 0.0.14
Requires:	gtk+2-devel >= 1:2.0.0
Requires:	libggz-devel >= 0.0.14

%description devel
Header files for ggz-gtk library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki ggz-gtk.

%package static
Summary:	Static ggz-gtk library
Summary(pl.UTF-8):	Statyczna biblioteka ggz-gtk
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ggz-gtk library.

%description static -l pl.UTF-8
Statyczna biblioteka ggz-gtk.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4 -I m4/ggz
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS QuickStart.GGZ README* TODO
%attr(755,root,root) %{_bindir}/ggz-gtk
%attr(755,root,root) %{_libdir}/libggz-gtk.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libggz-gtk.so.1
%{_datadir}/ggz/*
%{_desktopdir}/ggz-gtk.desktop
%{_mandir}/man6/ggz-gtk.6*
%{_pixmapsdir}/%{name}.xpm

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libggz-gtk.so
%{_libdir}/libggz-gtk.la
%{_includedir}/ggz-embed.h
%{_includedir}/ggz-gtk.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libggz-gtk.a
