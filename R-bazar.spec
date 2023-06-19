#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-bazar
Version  : 1.0.11
Release  : 42
URL      : https://cran.r-project.org/src/contrib/bazar_1.0.11.tar.gz
Source0  : https://cran.r-project.org/src/contrib/bazar_1.0.11.tar.gz
Summary  : Miscellaneous Basic Functions
Group    : Development/Tools
License  : GPL-3.0
Requires: R-kimisc
BuildRequires : R-kimisc
BuildRequires : buildreq-R

%description
copying objects to the clipboard ('Copy');
    manipulating strings ('concat', 'mgsub', 'trim', 'verlan'); 
    loading or showing packages ('library_with_dep', 'require_with_dep', 
    'sessionPackages'); 
    creating or testing for named lists ('nlist', 'as.nlist', 'is.nlist'), 
    formulas ('is.formula'), empty objects ('as.empty', 'is.empty'), 
    whole numbers ('as.wholenumber', 'is.wholenumber'); 
    testing for equality ('almost.equal', 'almost.zero') and computing 
    uniqueness ('almost.unique'); 
    getting modified versions of usual functions ('rle2', 'sumNA'); 
    making a pause or a stop ('pause', 'stopif'); 
    converting into a function ('as.fun');

%prep
%setup -q -c -n bazar
cd %{_builddir}/bazar

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640976514

%install
export SOURCE_DATE_EPOCH=1640976514
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bazar
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bazar
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bazar
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc bazar || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/bazar/DESCRIPTION
/usr/lib64/R/library/bazar/INDEX
/usr/lib64/R/library/bazar/Meta/Rd.rds
/usr/lib64/R/library/bazar/Meta/features.rds
/usr/lib64/R/library/bazar/Meta/hsearch.rds
/usr/lib64/R/library/bazar/Meta/links.rds
/usr/lib64/R/library/bazar/Meta/nsInfo.rds
/usr/lib64/R/library/bazar/Meta/package.rds
/usr/lib64/R/library/bazar/NAMESPACE
/usr/lib64/R/library/bazar/NEWS.md
/usr/lib64/R/library/bazar/R/bazar
/usr/lib64/R/library/bazar/R/bazar.rdb
/usr/lib64/R/library/bazar/R/bazar.rdx
/usr/lib64/R/library/bazar/help/AnIndex
/usr/lib64/R/library/bazar/help/aliases.rds
/usr/lib64/R/library/bazar/help/bazar.rdb
/usr/lib64/R/library/bazar/help/bazar.rdx
/usr/lib64/R/library/bazar/help/paths.rds
/usr/lib64/R/library/bazar/html/00Index.html
/usr/lib64/R/library/bazar/html/R.css
/usr/lib64/R/library/bazar/tests/testthat.R
/usr/lib64/R/library/bazar/tests/testthat/test-almost.zero.R
/usr/lib64/R/library/bazar/tests/testthat/test-is.empty.R
/usr/lib64/R/library/bazar/tests/testthat/test-is.formula.R
/usr/lib64/R/library/bazar/tests/testthat/test-is.wholenumber.R
/usr/lib64/R/library/bazar/tests/testthat/test-nin.R
/usr/lib64/R/library/bazar/tests/testthat/test-nlist.R
