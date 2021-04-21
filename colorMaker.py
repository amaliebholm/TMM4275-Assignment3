# NX 1957
# Journal created by Kasper on Mon Apr 19 22:09:47 2021 Vest-Europa (sommertid)
#
import math
import NXOpen
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    # ----------------------------------------------
    #   Menu: Edit->Object Display...
    # ----------------------------------------------
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    theSession.SetUndoMarkName(markId1, "Object Color Dialog")
    
    # ----------------------------------------------
    #   Dialog Begin Object Color
    # ----------------------------------------------
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Object Color")
    
    theSession.DeleteUndoMark(markId2, None)
    
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Object Color")
    
    theSession.DeleteUndoMark(markId3, None)
    
    theSession.SetUndoMarkName(markId1, "Object Color")
    
    theSession.DeleteUndoMark(markId1, None)
    
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Edit Object Display")
    
    displayModification1 = theSession.DisplayManager.NewDisplayModification()
    
    displayModification1.ApplyToAllFaces = True
    
    displayModification1.ApplyToOwningParts = False
    
    displayModification1.NewColor = 108
    
    objects1 = [NXOpen.DisplayableObject.Null] * 1 
    body1 = workPart.Bodies.FindObject("BLOCK(11)")
    objects1[0] = body1
    displayModification1.Apply(objects1)
    
    nErrs1 = theSession.UpdateManager.DoUpdate(markId4)
    
    displayModification1.Dispose()
    # ----------------------------------------------
    #   Menu: Edit->Object Display...
    # ----------------------------------------------
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    theSession.SetUndoMarkName(markId5, "Object Color Dialog")
    
    # ----------------------------------------------
    #   Dialog Begin Object Color
    # ----------------------------------------------
    markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Object Color")
    
    theSession.DeleteUndoMark(markId6, None)
    
    markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Object Color")
    
    theSession.DeleteUndoMark(markId7, None)
    
    theSession.SetUndoMarkName(markId5, "Object Color")
    
    theSession.DeleteUndoMark(markId5, None)
    
    markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Edit Object Display")
    
    displayModification2 = theSession.DisplayManager.NewDisplayModification()
    
    displayModification2.ApplyToAllFaces = True
    
    displayModification2.ApplyToOwningParts = False
    
    displayModification2.NewColor = 186
    
    objects2 = [NXOpen.DisplayableObject.Null] * 1 
    body2 = workPart.Bodies.FindObject("BLOCK(15)")
    objects2[0] = body2
    displayModification2.Apply(objects2)
    
    nErrs2 = theSession.UpdateManager.DoUpdate(markId8)
    
    displayModification2.Dispose()
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()