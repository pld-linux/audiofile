Summary:	Audio File Library - SGI Audio File Library
Summary(es):	Biblioteca para manipulación de varios archivos de sonido
Summary(pl):	Biblioteka Audio File - implementacja SGI Audio File Library
Summary(pt_BR):	Biblioteca para manipular vários formatos de arquivos de áudio
Name:		audiofile
Version:	0.2.3
Release:	3
Epoch:		1
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.68k.org./pub/michael/%{name}-%{version}.tar.gz
URL:		http://www.68k.org/~michael/audiofile/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libaudiofile
Obsoletes:	libaudiofile0

%description
This Audio File Library is an implementation of the SGI Audio File
library. Since the latter is specified ambiguously in places, I've
taken some liberties in interpreting certain such ambiguities. At the
present, not all features of the SGI Audio File library are
implemented. I feel, though, that this implementation of the Audio
File Library offers enough functionality to be useful for general
tasks. This library allows the processing of audio data to and from
audio files of many common formats (currently AIFF, AIFC, WAVE, and
NeXT/Sun).

%description -l es
La Biblioteca de Archivos de Audio es una implementación parcial de la
biblioteca de Archivos de Audio SGI. Dicha biblioteca permite el
procesado de datos de audio desde y para archivos de audio de los
formatos más comunes (actualmente AIFF, AIFC, WAVE, y NeXT/Sun).

Este software no está completo y está todavía desarrollándose. Muchos
formatos de archivo de sonido funcionan correctamente. Otros no tanto.

%description -l pl
Biblioteka Audio File jest implementacj± biblioteki SGI Audio File.
Przy jej pomocy mo¿na przetwarzaæ d¼wiêki w ró¿nych formatach (AIFF,
AIFC, WAVE i NeXT/Sun).

%description -l pt_BR
A biblioteca Audio File é uma implementação parcial da bibliotca Audio
File da SGI. Ela provê processamento de dados de áudio de e para
vários formatos comuns (atualmente AIFF, AIFC, WAVE e NeXT/Sun).

Este software não está completo e ainda está em desenvolvimento.
Muitos formatos funcionam bem, outros ainda não.

%package progs
Summary:	Audiofile programs
Summary(es):	Audiofile programs
Summary(pl):	Programy audiofile
Summary(pt_BR):	Programas que acompanham a biblioteca audiofile
Group:		Applications/Sound

%description progs
audiofile applications.

%description progs -l es
Audiofile programs.

%description progs -l pl
Programy audiofile.

%description progs -l pt_BR
Programas que acompanham a audiofile.

%package devel
Summary:	Header files and others to develop Audio File applications
Summary(es):	Bibliotecas, archivos de inclusión y otros archivos para el desarrollo de aplicaciones audiofile
Summary(pl):	Pliki nag³ówkowe i inne potrzebe do Audio File
Summary(pt_BR):	Bibliotecas, arquivos de inclusão e outros arquivos para desenvolver aplicativos audiofile
Group:		Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	libaudiofile-devel
Obsoletes:	libaudiofile0-devel

%description devel
Header files and others to develop Audio File applications.

%description devel -l pl
Pliki nag³ówków do Audio File'a, czyli to czego potrzebujesz do
tworzenia aplikacji pod Audio File'm.

%description devel -l es
Bibliotecas, archivos de inclusión y otros archivos para el desarrollo
de aplicaciones audiofile.

%description devel -l pt_BR
Bibliotecas, arquivos de inclusão e outros arquivos para desenvolver
aplicativos audiofile.

%package static
Summary:	Static libaudiofile libraries
Summary(es):	Static libraries for audiofile development
Summary(pl):	Biblioteka statyczne libaudiofile
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com audiofile
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}
Obsoletes:	libaudiofile-static

%description static
Static libaudiofile libraries.

%description static -l es
Static libraries for audiofile development

%description static -l pl
Biblioteki statyczne libaudiofile.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento com audiofile

%prep
%setup -q

%build
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir} \
	pkgconfig=%{_pkgconfigdir}

gzip -9nf NOTES README TODO

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {NOTES,README,TODO}.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sfconvert
%attr(755,root,root) %{_bindir}/sfinfo

%files devel
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/audiofile-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la

%{_includedir}/*
%{_aclocaldir}/audiofile.m4
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
