Summary:	Audio File Library - SGI Audio File Library
Summary(pl):	Biblioteka Audio File - implementacja SGI Audio File Library
Name:		audiofile
Version:	0.1.7
Release:	1
Copyright:	GPL
Group:		Applications/Sound
Group(pl):	Aplikacje/D¼wiêk
Source:		ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.gz
URL:		http://www.68k.org./~michael/audiofile/
BuildRoot:	/tmp/%{name}-%{version}-root
Obsoletes:	libaudiofile

%description
This Audio File Library is an implementation of the SGI Audio File library. 
Since the latter is specified ambiguously in places, I've taken some
liberties in interpreting certain such ambiguities. At the present, not all
features of the SGI Audio File library are implemented. I feel, though,
that this implementation of the Audio File Library offers enough
functionality to be useful for general tasks.

This library allows the processing of audio data to and from audio files of
many common formats (currently AIFF, AIFC, WAVE, and NeXT/Sun).

%description -l pl
Biblioteka Audio File jest implementacj± biblioteki SGI Audio File.
Przy jej pomocy mo¿na przetwarzaæ d¼wiêki w ró¿nych formatach (AIFF, AIFC,
WAVE i NeXT/Sun).

%package devel
Summary:	Header files and others to develop Audio File applications
Summary(pl):	Pliki nag³ówkowe i inne potrzebe do Audio File
Group:		Development/Libraries
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
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}
Obsoletes:	libaudiofile-static

%description static
Static libaudiofile libraries

%description -l pl devel
Biblioteki statyczne libaudiofile.

%prep
%setup -q

%build
autoconf
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target} \
	--prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf NOTES README TODO

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {NOTES,README,TODO}.gz

%attr(755,root,root) /usr/bin/sfconvert
%attr(755,root,root) /usr/bin/sfinfo
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)

%attr(755,root,root) /usr/bin/audiofile-config
%attr(755,root,root) %{_libdir}/lib*.so

/usr/include/*
%{_datadir}/aclocal/audiofile.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%changelog
* Wed Apr 21 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [0.1.6-2]
- removed "Conflicts: glibc <= 2.0.7" (not neccessary now),
- recompiled on rpm 3.

* Wed Mar 10 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.1.6-1]
- back to old name .. audiofile.

* Fri Feb 26 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.1.5-3]
- added "Conflicts: glibc <= 2.0.7" for prevent install
  with proper version glibc,
- changed Group in devel and static.

* Mon Jan 04 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.1.5-1d]
- changed package name to libaudiofile (audiofile added to Obsoletes),
- added striping shared libraries,
- audiofile-config to devel,
- enhanced main %description,
- added static subpackage,
- new %insatall and %build (libaudiofile have new autoconf scheme).

* Sun Sep 27 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.1.3-2]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- changed install prefix from /usr/local to /usr.
- changeded dependences to "Requires: %%{name} = %%{version}" in devel
  subpackage,
- added using $RPM_OPT_FLAGS during compile,
- added full %attr description in %files,
- simplifications in %install.

* Tue Aug 11 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.1.3-1]
- first try at an RPM,
- build against GNU libc-2.1.
