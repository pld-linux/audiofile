Summary:	Audio File Library - SGI Audio File Library
Summary(pl):	Biblioteka Audio File - implementacja SGI Audio File Library
Name:		audiofile
Version:	0.1.9
Release:	4
License:	GPL
Group:		Applications/Sound
Group(pl):	Aplikacje/D¼wiêk
Source:		ftp://ftp.gnome.org/pub/GNOME/sources/audiofile/%{name}-%{version}.tar.gz
URL:		http://www.68k.org/~michael/audiofile/
BuildRoot:	/tmp/%{name}-%{version}-root
Obsoletes:	libaudiofile

%description
This Audio File Library is an implementation of the SGI Audio File library.
 Since the latter is specified ambiguously in places, I've taken some
liberties in interpreting certain such ambiguities. At the present, not all
features of the SGI Audio File library are implemented. I feel, though,
that this implementation of the Audio File Library offers enough
functionality to be useful for general tasks. This library allows the
processing of audio data to and from audio files of many common formats
(currently AIFF, AIFC, WAVE, and NeXT/Sun).

%description -l pl
Biblioteka Audio File jest implementacj± biblioteki SGI Audio File. Przy
jej pomocy mo¿na przetwarzaæ d¼wiêki w ró¿nych formatach (AIFF, AIFC, WAVE
i NeXT/Sun).

%package devel
Summary:	Header files and others to develop Audio File applications
Summary(pl):	Pliki nag³ówkowe i inne potrzebe do Audio File
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}
Obsoletes:	libaudiofile-devel

%description devel
Header files and others to develop Audio File applications.

%description -l pl devel
Pliki nag³ówków do Audio File'a, czyli to czego potrzebujesz do tworzenia
aplikacji pod Audio File'm.

%package static
Summary:	Static libaudiofile libraries
Summary(pl):	Biblioteka statyczne libaudiofile
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}
Obsoletes:	libaudiofile-static

%description static
Static libaudiofile libraries.

%description -l pl static
Biblioteki statyczne libaudiofile.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*
strip $RPM_BUILD_ROOT%{_bindir}/{sfconvert,sfinfo}

gzip -9nf NOTES README TODO

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {NOTES,README,TODO}.gz

%attr(755,root,root) %{_bindir}/sfconvert
%attr(755,root,root) %{_bindir}/sfinfo
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/audiofile-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la

%{_includedir}/*
%{_datadir}/aclocal/audiofile.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
