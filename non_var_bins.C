#include "RooWorkspace.h"
#include "RooAbsPdf.h"
#include "RooDataSet.h"
#include "RooFitResult.h"
#include "RooPlot.h"
#include "RooRealVar.h"
#include "RooRandom.h"
#include "RooStats/ModelConfig.h"
using namespace RooFit; 
void deltarr()
{
   RooWorkspace w("w"); 
   w.factory("x[0,4]");  

   w.factory("nbackground[195, 0, 1950]"); 
   w.factory("nsignal[18, 0.0, 180]");

   w.factory("mean [1]");
   w.factory("sigma[0.6]");// mean + 5 sigma=4 // 
   w.factory("Gaussian::bmodel(x, mean, sigma)");
   w.factory("Gaussian::smodel(x, mean, sigma)");

   w.factory("SUM::model(nbackground*bmodel, nsignal*smodel)");
   RooAbsPdf *pdf  = w.pdf("model");

   RooRealVar  x("x","x",0,4) ;

   RooRandom::randomGenerator()->SetSeed(0);

   bool aprioriBinning(true);
   if(aprioriBinning)
     {
       RooBinning b(0,4);
       b.addUniform(5,0,2.2);// 95% events in 2 sigma, for 10% --> stat. is constrained to 15% if number of bins/ number of events = 0.15^2//
       b.addUniform(1,2.2,4);// 5% events at the tail of dist. --> stat. is constrained to 25% if --//-- = 0.25^2 //
       
       x.setBinning(b);
       RooDataSet * data   = pdf->generate(RooArgSet(x),AllBinned());
       RooDataSet * datac  = (RooDataSet*) data ->reduce(Cut("x > 0.4"));
       
       datac->SetName("datac");
       w.import(*datac);
       datac->Print();
       RooPlot * plot = x.frame(Title("x=min_Delta_R in 3ll"));
       datac->plotOn(plot,Binning(b)) ;
       //   pdf->plotOn(plot);
       cout << ">> number of bins: " << datac->numEntries() << endl ;
       for(Int_t i=0 ;i< datac->numEntries();i++)
	 {	
	   datac->get(i);
	   Double_t c = datac->weight(); 
	   Double_t d = sqrt(c); 
	   Double_t e = d/c; 
	   cout << "n("<<i<<"):"  << c << "-->"<< d << "-->" << e*100 <<"%"<< endl;
	 }
       plot->Draw();
     }
}


void non_var_bins(TString var="deltar"){
  if(var=="deltar")
    deltarr();
  else
    cout << "This variable is not implemented yet. Have a nice day" << endl;

  gApplication->Terminate();
}
