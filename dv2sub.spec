Name:          dv2sub
Version:       0.3
Release:       1
Summary:       DV subtitle extractor
URL:           http://%{name}.sourceforge.net
License:       GPLv2
Group:         Video
Source0:       http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires: pkgconfig
BuildRequires: libdv-devel

%description
This simple utility is usable for creating MicroDVD subtitles with date and
time of recording extracted from raw DV stream (using GPL codec LibDV for DV
video. Extracting of some other basic information is also possible
(may be more information later).
Dv2sub can read DV stream from stdin or from file using mmap if available.
Mmap input is faster than sequential read of whole DV data stream.
Dv2sub can be used in pass through mode
(DV stream is read from stdin and output to stdout) usable for one
pass DV recoding to other video format and subtitles extraction in one step.

%prep
%autosetup

%build
./configure --prefix=%{_prefix}
%make_build

%install
%make_install

%files
%doc AUTHORS ChangeLog
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
