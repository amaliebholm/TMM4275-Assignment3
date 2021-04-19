# NX 1957
# Journal created by Kasper on Fri Apr 16 11:11:44 2021 Vest-Europa (sommertid)
#
import math
import NXOpen
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    partCloseResponses1 = theSession.Parts.NewPartCloseResponses()
    
    workPart.Close(NXOpen.BasePart.CloseWholeTree.FalseValue, NXOpen.BasePart.CloseModified.UseResponses, partCloseResponses1)
    
    workPart = NXOpen.Part.Null
    displayPart = NXOpen.Part.Null
    partCloseResponses1.Dispose()
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Change Displayed Part")
    
    part1 = theSession.Parts.FindObject("model1")
    status1, partLoadStatus1 = theSession.Parts.SetActiveDisplay(part1, NXOpen.DisplayPartOption.AllowAdditional, NXOpen.PartDisplayPartWorkPartOption.UseLast)
    
    workPart = theSession.Parts.Work # model1
    displayPart = theSession.Parts.Display # model1
    partLoadStatus1.Dispose()
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()