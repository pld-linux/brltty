# TODO:
#	- what is that huge %post script?
#	- ocaml bcond is useless now:
#		Cannot find ocamlfind.
#		BrlAPI Caml bindings will be compiled but not installed.
#	- check java stuff
#	- create bcond to build with minimal deps (wo ncurses,gpm,at-spi*)
#
# warning: Installed (but unpackaged) file(s) found:
#    /usr/lib/ocaml/brlapi/META
#    /usr/lib/ocaml/brlapi/brlapi.cma
#    /usr/lib/ocaml/brlapi/brlapi.cmi
#    /usr/lib/ocaml/brlapi/brlapi.cmxa
#    /usr/lib/ocaml/brlapi/brlapi.mli
#    /usr/lib/ocaml/brlapi/libbrlapi_stubs.a
#    /usr/lib/ocaml/stublibs/dllbrlapi_stubs.so
#    /usr/lib/ocaml/stublibs/dllbrlapi_stubs.so.owner
#    /usr/share/man/man1/xbrlapi.1.gz
#
# Conditional build:
%bcond_without	apidocs		# documentation generated with doxygen
%bcond_with	java		# java bindings
%bcond_with	ocaml		# ocaml bindings (NFY)
%bcond_without	python		# python bindings
%bcond_without	tcl		# tcl bindings
%bcond_without	x		# build X11-based utilities
#
%include	/usr/lib/rpm/macros.java
Summary:	Braille display driver for Linux/Unix
Summary(pl.UTF-8):	Sterownik do wyświetlaczy Braille'a
Name:		brltty
Version:	4.2
Release:	0.1
Group:		Daemons
License:	GPL
Source0:	http://mielke.cc/brltty/releases/%{name}-%{version}.tar.gz
# Source0-md5:	192af5e634210616928496645e392097
Patch0:		%{name}-ac.patch
URL:		http://mielke.cc/brltty/
BuildRequires:	at-spi-devel
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake
BuildRequires:	bison
#BuildRequires:	bluez-devel
%{?with_apidocs:BuildRequires:	doxygen}
BuildRequires:	gpm-devel
%{?with_java:BuildRequires:	jdk}
BuildRequires:	ncurses-devel
%{?with_ocaml:BuildRequires:	ocaml}
BuildRequires:	pkgconfig
%{?with_python:BuildRequires:	python-Pyrex}
%{?with_java:BuildRequires:	rpm-javaprov}
%{?with_python:BuildRequires:	rpm-pythonprov}
%{?with_tcl:BuildRequires:	tcl}
%{?with_x:BuildRequires:	xorg-lib-libXaw-devel}
%{?with_x:BuildRequires:	xorg-lib-libXtst-devel}
# libbrlttyblb
#BR: libbraile-devel (-lllibbraile <braille.h>)
# libbrlttysfl
BuildRequires:	flite-devel
# libbrlttysmp
#BR: Mikropuhe-devel (-lmikropuhe <mpwrfile.h>)
# libbrlttyssd
#BuildRequires:	speech-dispatcher-devel
# libbrlttyssw
#BR: Swift-devel (-lswift <swift.h>)
# libbrlttysth
#BR: Theta-devel (-ltheta <theta.h>)
# libbrlttysvv
#BR: ViaVoice-devel (-lviavoice <eci.h>)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BRLTTY is a background process (daemon) which provides access to the
Linux/Unix console (when in text mode) for a blind person using a
refreshable Braille display. It drives the Braille display, and
provides complete screen review functionality. Some speech capability
has also been incorporated.

%description -l pl.UTF-8
BRLTTY jest demonem, który udostępnia dostęp do linuksowej konsoli (w
trybie tekstowym) dla niewidomych używających wyświetlaczy Braille'a z
odświeżaniem (refreshable Braille display). BRLTTY steruje
wyświetlaczem Braille'a i dostarcza funkcjonalność całkowitego
przeglądu ekranu. Do tego pakietu została włączona możliwość syntezy
mowy.

%package -n brlapi
Summary:	Application Programming Interface for BRLTTY
Summary(pl.UTF-8):	API do BRLTTY
Group:		Applications/System

%description -n brlapi
This package provides the run-time support for the Application
Programming Interface to BRLTTY.

Install this package if you have an application which directly
accesses a refreshable Braille display.

%description -n brlapi -l pl.UTF-8
Ten pakiet zawiera środowisko uruchomieniowe dla programów
korzystających z API BRLTTY.

Zainstaluj ten pakiet jeśli masz aplikację, która bezpośrednio używa
wyświetlacza Braille'a z odświeżaniem.

%package -n brlapi-devel
Summary:	Headers and documentation for BrlAPI
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do BrlAPI
Group:		Development/Libraries
Requires:	brlapi = %{version}-%{release}

%description -n brlapi-devel
This package provides the header files, shared object linker
reference, and reference documentation for BrlAPI (the Application
Programming Interface to BRLTTY). It enables the implementation of
applications which take direct advantage of a refreshable Braille
display in order to present information in ways which are more
appropriate for blind users and/or to provide user interfaces which
are more specifically atuned to their needs.

Install this package if you're developing or maintaining an
application which directly accesses a refreshable Braille display.

%description -n brlapi-devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe oraz dokumentację do BrlAPI (API
do BRLTTY). BrlAPI pozwala implementować aplikacje, które bezpośrednio
korzystają z wyświetlaczy Braille'a dostarczając interfejs użytkownika
bardziej przystosowany dla osób niewidomych.

Zainstaluj ten pakiet, jeśli tworzysz lub nadzorujesz aplikację
korzystającą bezpośrednio z odświeżalnych wyświetlaczy Braille'a.

%package -n brlapi-static
Summary:	Static BrlAPI library
Summary(pl.UTF-8):	Statyczna biblioteka BrlAPI
Group:		Development/Libraries
Requires:	brlapi-devel = %{version}-%{release}

%description -n brlapi-static
This is package with static BrlAPI library.

%description -n brlapi-static -l pl.UTF-8
Ten pakiet zawiera statyczną wersję biblioteki BrlAPI.

%package -n brlapi-apidocs
Summary:	BrlAPI documentation
Summary(pl.UTF-8):	Documentacja BrlAPI
Group:		Documentation

%description -n brlapi-apidocs
Documentation for BrlAPI in HTML format generated from brltty
sources by doxygen.

%description -n brlapi-apidocs -l pl.UTF-8
Dokumentacja BrlAPI w formacie HTML generowane ze
źrodeł brltty przez doxygen.

%package -n java-brlapi
Summary:	BrlAPI library for Java
Summary(pl.UTF-8):	Biblioteka BrlAPI dla Javy
Group:		Libraries
Requires:	brlapi = %{version}-%{release}

%description -n java-brlapi
BrlAPI library for Java.

%description -n java-brlapi -l pl.UTF-8
Biblioteka BrlAPI dla Javy.

%package -n python-brlapi
Summary:	Python interface to BrlAPI
Summary(pl.UTF-8):	Pythonowy interfejs do BrlAPI
Group:		Libraries
Requires:	brlapi = %{version}-%{release}

%description -n python-brlapi
Python interface to BrlAPI.

%description -n python-brlapi -l pl.UTF-8
Pythonowy interfejs do BrlAPI.

%package -n brlapi-tcl
Summary:	BrlAPI library for Tcl
Summary(pl.UTF-8):	Biblioteka BrlAPI dla Tcl
Group:		Libraries
Requires:	brlapi = %{version}-%{release}

%description -n brlapi-tcl
BrlAPI library for Tcl.

%description -n brlapi-tcl -l pl.UTF-8
Biblioteka BrlAPI dla Tcl.

%prep
%setup -q
#%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
cp -f /usr/share/automake/config.sub acdir
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%configure \
	--with-install-root="$RPM_BUILD_ROOT" \
	--disable-tainted-components \
	%{!?with_java:--disable-java-bindings} \
	--enable-api
%{__make}

directory="doc"
mkdir -p "$directory"
for file in `find . \( -path "./$directory" -o -path ./Documents \) -prune -o \( -name 'README*' -o -name '*.txt' -o -name '*.html' -o -name '*.sgml' -o \( -path "./Bootdisks/*" -type f -perm +ugo=x \) \) -print`
do
	mkdir -p "$directory/${file%/*}"
	cp -rp "$file" "$directory/$file"
done

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -j1 install
install Documents/brltty.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%pre
# The pre-install scriptlet.

# If a configuration file already exists then rpm installs the new one as
# <path>.rpmnew. If this is done then the .rpmnew file is overwritten if it
# already exists.

# There's no explicit way to tell if a configuration file has been installed
# as itself or as a .rpmnew file. The way we'll figure it out, therefore, is by
# erasing the .rpmnew file now so that we can see if it gets created later.
rm -f "%{_sysconfdir}/brltty.conf.rpmnew"

%post
# The post-install scriptlet.

# If BRLTTY's boot parameter has been specified then update the just installed
# configuration file template to reflect the options supplied thereby.

# First, we need to determine which file to update. If there's a .rpmnew file
# then update it since a previous configuration file must already have existed.
file="%{_sysconfdir}/brltty.conf"
new="${file}.rpmnew"
[ -f "${new}" ] && file="${new}"

# Update the configuration file template via the Bootdisks/bp2cf script.
# Include it right within this scriptlet so that it needn't be installed.
# Imbed it within a subshell to ensure that it won't impact this scriptlet.
(
	# First, set bp2cf's command line arguments.
	set -- -u -f "${file}"

#!/bin/sh
###############################################################################
# BRLTTY - A background process providing access to the Linux console (when in
#          text mode) for a blind person using a refreshable Braille display.
#
# Copyright (C) 1995-2003 by The BRLTTY Team. All rights reserved.
#
# BRLTTY comes with ABSOLUTELY NO WARRANTY.
#
# This is free software, placed under the terms of the
# GNU General Public License, as published by the Free Software
# Foundation.  Please see the file COPYING for details.
#
# Web Page: http://mielke.cc/brltty/
#
# This software is maintained by Dave Mielke <dave@mielke.cc>.
###############################################################################

# Convert the boot parameter to configuration file directives.
# If /proc is mounted then use the brltty= boot parameter in /proc/cmdline.
# If /proc is not mounted then use the brltty environment variable.
# Invoke with -h for usage information.

programName="${0##*/}"
programMessage()
{
	echo 2>&1 "${programName}: ${1}"
}
syntaxError()
{
	programMessage "${1}"
	exit 2
}
internalError()
{
	programMessage "${1}"
	exit 3
}

configurationFile=""
requestedAction=create
deviceTranslation=none
requestedParameter=""
OPTIND=1
while getopts ":f:cundop:h" option
do
	case "${option}" in
	    f) configurationFile="${OPTARG}";;
	    c) requestedAction=create;;
	    u) requestedAction=update;;
	    n) deviceTranslation=none;;
	    d) deviceTranslation=devfs;;
	    o) deviceTranslation=old;;
	    p) requestedParameter="${OPTARG}";;
	    h)
		cat <<EOF
Usage: ${programName} [option ...]
-f file  The configuration file to create/update.
-c       Create the configuration file (write to stdout if no -f).
-u       Update the configuration file (copying from stdin to stdout if no -f).
-n       Do not translate device paths.
-d       Do old-style to devfs device path translation.
-o       Do devfs to old-style device path translation.
-p [driver][,[device][,[table]]]
         Explicitly specify the boot parameter.
-h       Display this usage summary.
EOF
		exit 0
		;;
	    \?) syntaxError "unknown option: -${OPTARG}";;
	    :) syntaxError "missing value: -${OPTARG}";;
	    *) internalError "unimplemented option: -${option}";;
	esac
done
shift "`expr $OPTIND - 1`"
[ "${#}" -eq 0 ] || syntaxError "too many parameters."

case "${requestedAction}" in
    create)
	putConfigurationLine()
	{
		echo "${1}" || exit 4
	}
	startConfigurationFile()
	{
		[ -n "${configurationFile}" ] && exec >"${configurationFile}"
		putConfigurationLine "`makeHeaderLine Created`"
		putConfigurationLine "`makeParameterLine`"
		putConfigurationLine ""
	}
	putConfigurationDirective()
	{
		putConfigurationLine "${1} ${2}"
	}
	finalizeConfigurationFile()
	{
		:
	}
	;;
    update)
	putSedCommand()
	{
		sedScript="${sedScript}
${1}"
	}
	startConfigurationFile()
	{
		if [ -n "${configurationFile}" ]; then
			[ -e "${configurationFile}" ] || syntaxError "file not found: ${configurationFile}"
			[ -f "${configurationFile}" ] || syntaxError "not a file: ${configurationFile}"
			[ -r "${configurationFile}" ] || syntaxError "file not readable: ${configurationFile}"
			[ -w "${configurationFile}" ] || syntaxError "file not writable: ${configurationFile}"
			outputFile="${configurationFile}.new"
			exec <"${configurationFile}" >"${outputFile}"
		fi
		sedScript=""
		putSedCommand "1i\\
`makeHeaderLine Updated`\\
`makeParameterLine`\\
"
	}
	putConfigurationDirective()
	{
		value="`echo "${2}" | sed -e 's%\\([/\\]\\)%\\\\\\1%g'`"
		putSedCommand "/^ *#\\(${1} .*\\)/s//\\1/"
		putSedCommand "/^ *\\(${1}\\) .*/s//\\1 ${value}/"
	}
	finalizeConfigurationFile()
	{
		sed -e "${sedScript}"
		[ -n "${outputFile}" ] && mv -f "${outputFile}" "${configurationFile}"
	}
	;;
    *) internalError "unimplemented action: ${requestedAction}";;
esac

translateDevice_none()
{
	:
}
translateDevice_devfs()
{
	minor="${device#ttyS}"
	if [ "${minor}" != "${device}" ]; then
		device="tts/${minor}"
		return 0
	fi
	minor="${device#lp}"
	if [ "${minor}" != "${device}" ]; then
		device="printers/${minor}"
		return 0
	fi
	programMessage "unsupported old-style device: ${device}"
}
translateDevice_old()
{
	major="${device%%/*}"
	if [ "${major}" != "${device}" ]; then
		minor="${device#*/}"
		case "${major}" in
		    tts) devfs="ttyS${minor}";;
		    printers) devfs="lp${minor}";;
		esac
	fi
	if [ -n "${devfs}" ]; then
		device="${devfs}"
	else
		programMessage "unsupported devfs device: ${device}"
	fi
}

makeHeaderLine()
{
	echo "# ${1} by brltty-bp2cf`date +' on %Y-%m-%d at %H:%M:%S %Z (UTC%z)'`."
}
makeParameterLine()
{
	echo "# Boot Parameter:${bootParameter}"
}
putConfigurationFile()
{
	startConfigurationFile
	[ -n "${brailleDriver}" ] && putConfigurationDirective "braille-driver" "${brailleDriver}"
	[ -n "${brailleDevice}" ] && {
	device="`echo "${brailleDevice}" | sed -e 's%//*%/%g' -e 's%^/dev/%%'`"
	if [ "${device#/}" = "${device}" ]; then
		translateDevice_${deviceTranslation}
	fi
	putConfigurationDirective "braille-device" "${device}"
	}
	[ -n "${textTable}" ] && putConfigurationDirective "text-table" "${textTable}"
	finalizeConfigurationFile
}
parseBootParameter()
{
	bootParameter="${bootParameter} ${1}"
	number=1
	while [ "${number}" -le 3 ]; do
		cut="cut -d, -f${number}"
		[ "${number}" -gt 1 ] && cut="${cut} -s"
		operand="`echo ${1} | ${cut}`"
		if [ -n "${operand}" ]; then
			case "${number}" in
			    1) brailleDriver="${operand}";;
			    2) brailleDevice="${operand}";;
			    3) textTable="${operand}";;
			esac
		fi
		number="`expr ${number} + 1`"
	done
}
putBootParameter()
{
	parseBootParameter "${1}"
	putConfigurationFile
}
parseBootCommand()
{
	found=false
	while [ "${#}" -gt 0 ]; do
		case "${1}" in
		    "brltty="*)
			found=true
			parseBootParameter "${1#*=}"
			;;
		esac
		shift
	done
	"${found}" && putConfigurationFile
}

brailleDriver=""
brailleDevice=""
textTable=""
bootCommandFile="/proc/cmdline"
if [ -n "${requestedParameter}" ]; then
	putBootParameter "${requestedParameter}"
elif [ -f "${bootCommandFile}" ]; then
	parseBootCommand `cat "${bootCommandFile}"`
elif [ -n "${brltty}" ]; then
	putBootParameter "${brltty}"
fi
exit 0
)

%post	-n brlapi -p /sbin/ldconfig
%postun	-n brlapi -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Documents/{Manual-BRLTTY/English/BRLTTY*,ChangeLog,HISTORY,TODO}
%doc doc/{Bindings,Bootdisks,BrailleDrivers,BrailleTables,ContractionTables,Patches,README,SpeechDrivers}
%attr(755,root,root) %{_bindir}/brltty
%attr(755,root,root) %{_bindir}/brltty-install
%attr(755,root,root) %{_bindir}/brltty-config
%attr(755,root,root) %{_bindir}/vstp
%{?with_x:%attr(755,root,root) %{_bindir}/xbrlapi}
%dir %{_libdir}/brltty
%attr(755,root,root) %{_libdir}/brltty/libbrlttybal.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybat.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybba.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybbd.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybbl.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybbm.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybbn.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybbs.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybcb.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybec.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybeu.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybfs.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybht.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybil.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttyblt.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybmb.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybmd.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybmn.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybpm.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybtn.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybts.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybtt.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybvd.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybvo.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybvr.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybvs.so
%{?with_x:%attr(755,root,root) %{_libdir}/brltty/libbrlttybxw.so}
%attr(755,root,root) %{_libdir}/brltty/libbrlttysal.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttysbl.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttyscb.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttyses.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttysfl.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttysfv.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttysgs.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttyxas.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttyxlx.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttyxsc.so
%{_sysconfdir}/brltty
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/brltty.conf
%{_mandir}/man1/brltty.1*
%{_mandir}/man1/vstp.1*

%files -n brlapi
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbrlapi.so.0.5.2
%attr(755,root,root) %ghost %{_libdir}/libbrlapi.so.0.5

%files -n brlapi-devel
%defattr(644,root,root,755)
%doc Documents/README.Gnopernicus
%doc Documents/Manual-BrlAPI/English/BrlAPI*
%attr(755,root,root) %{_libdir}/libbrlapi.so
%{_includedir}/brltty
%{_includedir}/brlapi*.h
%{_mandir}/man3/*

%files -n brlapi-static
%defattr(644,root,root,755)
%{_libdir}/libbrlapi.a

%if %{with apidocs}
%files -n brlapi-apidocs
%defattr(644,root,root,755)
%doc Documents/BrlAPIref/html/*
%endif

%if %{with java}
%files -n java-brlapi
%defattr(644,root,root,755)
%{_libdir}/java/libbrlapi_java.so
%{_javadir}/brlapi.jar
%endif

%if %{with python}
%files -n python-brlapi
%defattr(644,root,root,755)
%{py_sitedir}/Brlapi-*.egg-info
%attr(755,root,root) %{py_sitedir}/brlapi.so
%endif

%if %{with tcl}
%files -n brlapi-tcl
%defattr(644,root,root,755)
%dir %{_libdir}/brlapi-0.5.2
%attr(755,root,root) %{_libdir}/brlapi-0.5.2/libbrlapi_tcl.so
%{_libdir}/brlapi-0.5.2/pkgIndex.tcl
%endif
