Summary:	Braille display driver for Linux/Unix
Summary(pl):	Sterownik do wy¶wietlaczy Braille'a
Name:		brltty
Version:	3.7.2
Release:	3
Group:		Daemons
License:	GPL
URL:		http://mielke.cc/brltty/
Source0:	http://mielke.cc/brltty/releases/%{name}-%{version}.tar.gz
# Source0-md5:	0ae3da8252783a4d20e1ed4e55cede5b
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	bison
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BRLTTY is a background process (daemon) which provides access to the
Linux/Unix console (when in text mode) for a blind person using a
refreshable Braille display. It drives the Braille display, and
provides complete screen review functionality. Some speech capability
has also been incorporated.

%description -l pl
BRLTTY jest demonem, który udostêpnia dostêp do linuksowej konsoli (w
trybie tekstowym) dla niewidomych u¿ywaj±cych wy¶wietlaczy Braille'a z
od¶wie¿aniem (refreshable Braille display). BRLTTY steruje
wy¶wietlaczem Braille'a i dostarcza funkcjonalno¶æ ca³kowitego
przegl±du ekranu. Do tego pakietu zosta³a w³±czona mo¿liwo¶æ syntezy
mowy.

%package -n brlapi
Summary:	Application Programming Interface for BRLTTY
Summary(pl):	API do BRLTTY
Group:		Applications/System

%description -n brlapi
This package provides the run-time support for the Application
Programming Interface to BRLTTY.

Install this package if you have an application which directly
accesses a refreshable Braille display.

%description -n brlapi -l pl
Ten pakiet zawiera ¶rodowisko uruchomieniowe dla programów
korzystaj±cych z API BRLTTY.

Zainstaluj ten pakiet je¶li masz aplikacjê, która bezpo¶rednio u¿ywa
wy¶wietlacza Braille'a z od¶wie¿aniem.

%package -n brlapi-devel
Summary:	Headers and documentation for BrlAPI
Summary(pl):	Pliki nag³ówkowe i dokumentacja do BrlAPI
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

%description -n brlapi-devel -l pl
Ten pakiet zawiera pliki nag³ówkowe oraz dokumentacjê do BrlAPI (API
do BRLTTY). BrlAPI pozwala implementowaæ aplikacje, które bezpo¶rednio
korzystaj± z wy¶wietlaczy Braille'a dostarczaj±c interfejs u¿ytkownika
bardziej przystosowany dla osób niewidomych.

Zainstaluj ten pakiet, je¶li tworzysz lub nadzorujesz aplikacjê
korzystaj±c± bezpo¶rednio z od¶wie¿alnych wy¶wietlaczy Braille'a.

%package -n brlapi-static
Summary:	Static BrlAPI library
Summary(pl):	Statyczna biblioteka BrlAPI
Group:		Development/Libraries
Requires:	brlapi-devel = %{version}-%{release}

%description -n brlapi-static
This is package with static BrlAPI library.

%description -n brlapi-static -l pl
Ten pakiet zawiera statyczn± wersjê biblioteki BrlAPI.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
cp -f /usr/share/automake/config.sub acdir
%configure \
	--with-install-root="$RPM_BUILD_ROOT" \
	--disable-tainted-components \
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
%{__make} install
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
%doc Documents/{Manual.sgml,Manual.txt,Manual-HTML,ChangeLog,TODO} doc/*
%attr(755,root,root) %{_bindir}/brltty
%attr(755,root,root) %{_bindir}/brltty-*
%attr(755,root,root) %{_bindir}/xbrlapi
%dir %{_libdir}/brltty
%dir %{_sysconfdir}/brltty
%attr(755,root,root) %{_libdir}/brltty/*.so
%dir %{_libdir}/brltty
%{_sysconfdir}/brltty
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/brltty.conf
%{_mandir}/man1/*

%files -n brlapi
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbrlapi.so.*
%doc Documents/BrlAPI.sgml Documents/BrlAPI.txt Documents/BrlAPI-HTML

%files -n brlapi-devel
%defattr(644,root,root,755)
%doc Documents/BrlAPIref-HTML Documents/README.Gnopernicus
%attr(755,root,root) %{_libdir}/libbrlapi.so
%{_includedir}/brltty
%{_mandir}/man3/*

%files -n brlapi-static
%defattr(644,root,root,755)
%{_libdir}/libbrlapi.a
