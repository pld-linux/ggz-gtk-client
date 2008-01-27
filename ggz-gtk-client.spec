Summary:	GTK+ version of GGZ client
Summary(pl.UTF-8):	Klient napisany w GTK+ dla GGZ
Name:		ggz-gtk-client
Version:	0.0.14
Release:	1
License:	GPL v2+
Group:		Applications/Games
Source0:	http://ftp.belnet.be/packages/ggzgamingzone/ggz/0.0.14/%{name}-%{version}.tar.gz
# Source0-md5:	7b8992f4eaf96c41923c31a946bc73fb
Source1:	%{name}.xpm
Patch0:		%{name}-desktop.patch
URL:		http://www.ggzgamingzone.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	ggz-client-libs-devel >= 0.0.14
BuildRequires:	gtk+2-devel
BuildRequires:	libggz-devel >= 0.0.14
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GGZ core clients enable players to access the GGZ server to chat, meet
other people in the game lobbies, play with them, watch their scores,
and be spectator other people's games. This is GTK+ version of GGZ
client.

%description -l pl.UTF-8
Klienty GGZ umożliwiają graczą dostęp do serwerów GGZ z
możliwością rozmowy, poznawania innych ludzi w grze, granie z nimi,
obserwowanie punktacji oraz obserwowanie rozgrywek innych ludzi. Ten
klient GGZ to wersja napisana w GTK+.

%package devel
Summary:	Header files for ggz-gtk-client
Summary(pl.UTF-8):	Pliki nag�~Bówkowe dla ggz-gtk-client
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for ggz-gtk-client.

%description devel -l pl.UTF-8
Pliki nag�~Bówkowe dla ggz-gtk-client.

%package static
Summary:	Static ggz-gtk-client library
Summary(pl.UTF-8):	Statyczna biblioteka ggz-gtk-client
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ggz-gtk-client library.

%description static -l pl.UTF-8
Statyczna biblioteka ggz-gtk-client.

%prep
%setup -q
%patch0 -p1

%build
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
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/lib*.so.1
%{_datadir}/ggz
%{_desktopdir}/ggz-gtk.desktop
%{_mandir}/man6/*.6*
%{_pixmapsdir}/%{name}.xpm

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
