Summary:	Audio File Library - SGI Audio File Library
Summary(es.UTF-8):   Biblioteca para manipulación de varios archivos de sonido
Summary(pl.UTF-8):   Biblioteka Audio File - implementacja SGI Audio File Library
Summary(pt_BR.UTF-8):   Biblioteca para manipular vários formatos de arquivos de áudio
Summary(ru.UTF-8):   Библиотека работы с разными форматами аудио-файлов
Summary(uk.UTF-8):   Бібліотека роботи з різними форматами аудіо-файлів
Name:		audiofile
Version:	0.2.6
Release:	4
Epoch:		1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/0.2/%{name}-%{version}.tar.bz2
# Source0-md5:	3d01302834660850b6141cac1e6f5501
Patch0:		%{name}-am18.patch
Patch1:		%{name}-less_mem_hungry.patch
URL:		http://www.68k.org/~michael/audiofile/
BuildRequires:	automake
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

%description -l es.UTF-8
La Biblioteca de Archivos de Audio es una implementación parcial de la
biblioteca de Archivos de Audio SGI. Dicha biblioteca permite el
procesado de datos de audio desde y para archivos de audio de los
formatos más comunes (actualmente AIFF, AIFC, WAVE, y NeXT/Sun).

Este software no está completo y está todavía desarrollándose. Muchos
formatos de archivo de sonido funcionan correctamente. Otros no tanto.

%description -l pl.UTF-8
Biblioteka Audio File jest implementacją biblioteki SGI Audio File.
Przy jej pomocy można przetwarzać dźwięki w różnych formatach (AIFF,
AIFC, WAVE i NeXT/Sun).

%description -l pt_BR.UTF-8
A biblioteca Audio File é uma implementação parcial da bibliotca Audio
File da SGI. Ela provê processamento de dados de áudio de e para
vários formatos comuns (atualmente AIFF, AIFC, WAVE e NeXT/Sun).

Este software não está completo e ainda está em desenvolvimento.
Muitos formatos funcionam bem, outros ainda não.

%description -l ru.UTF-8
Библиотека работы с разными форматами фудио-файлов. Используется
демоном esound.

%description -l uk.UTF-8
Бібліотека роботи з різними форматами аудіо-файлів. Використовується
демоном esound.

%package progs
Summary:	Audiofile programs
Summary(pl.UTF-8):   Programy audiofile
Summary(pt_BR.UTF-8):   Programas que acompanham a biblioteca audiofile
Group:		Applications/Sound

%description progs
audiofile applications.

%description progs -l pl.UTF-8
Programy audiofile.

%description progs -l pt_BR.UTF-8
Programas que acompanham a audiofile.

%package devel
Summary:	Header and other files to develop Audio File applications
Summary(es.UTF-8):   Archivos de inclusión y otros archivos para el desarrollo de aplicaciones audiofile
Summary(pl.UTF-8):   Pliki nagłówkowe i inne potrzebe do Audio File
Summary(pt_BR.UTF-8):   Arquivos de inclusão e outros arquivos para desenvolver aplicativos audiofile
Summary(ru.UTF-8):   Файлы для разработки приложений с использованием audiofile
Summary(uk.UTF-8):   Файли для розробки прикладних програм з використанням audiofile
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	libaudiofile-devel
Obsoletes:	libaudiofile0-devel

%description devel
Header and other files to develop Audio File applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Audio File, czyli to, co jest potrzebne do
tworzenia aplikacji korzystających z tej biblioteki.

%description devel -l es.UTF-8
Archivos de inclusión y otros archivos para el desarrollo de
aplicaciones audiofile.

%description devel -l pt_BR.UTF-8
Arquivos de inclusão e outros arquivos para desenvolver aplicativos
audiofile.

%description devel -l ru.UTF-8
.h-файлы и пр. для разработки приложений с использованием audiofile.

%description devel -l uk.UTF-8
.h-файли та інше для розробки прикладних програм з використанням
audiofile.

%package static
Summary:	Static libaudiofile libraries
Summary(pl.UTF-8):   Biblioteka statyczne libaudiofile
Summary(pt_BR.UTF-8):   Bibliotecas estáticas para desenvolvimento com audiofile
Summary(ru.UTF-8):   Статические библиотеки для разработки приложений с использованием audiofile
Summary(uk.UTF-8):   Статичні бібліотеки для розробки прикладних програм з використанням audiofile
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Obsoletes:	libaudiofile-static

%description static
Static libaudiofile libraries.

%description static -l pl.UTF-8
Biblioteki statyczne libaudiofile.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com audiofile

%description static -l ru.UTF-8
Статические библиотеки для разработки приложений с использованием
audiofile.

%description static -l uk.UTF-8
Статичні бібліотеки для розробки прикладних програм з використанням
audiofile.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cp /usr/share/automake/config.sub .
%configure \
	--enable-largefile
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NOTES README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sfconvert
%attr(755,root,root) %{_bindir}/sfinfo

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/audiofile-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_aclocaldir}/audiofile.m4
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
