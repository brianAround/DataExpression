select
    cd.JCCo, cd.Mth, cd.CostTrans, cd.KeyID, cd.Job, cd.PhaseGroup, cd.Phase, cd.CostType, cd.PostedDate, cd.ActualDate, cd.JCTransType, cd.[Source], cd.[Description], cd.ReversalStatus
    , cd.UM, cd.ActualUnitCost, cd.ActualHours, cd.ActualUnits, cd.ActualCost
    , cd.PRCo, cd.Employee, cd.Craft, cd.Class, cd.EarnFactor, cd.EarnType
    , cd.VendorGroup, cd.Vendor, cd.APCo, cd.APTrans, cd.APLine, cd.APRef
    , cd.PO, cd.POItem, cd.SL, cd.SLItem
    , cd.EMCo, cd.EMEquip, cd.EMRevCode, cd.EMGroup, cd.EMTrans
from JCCD cd
    inner join JCJM jm
        on jm.JCCo = cd.JCCo and jm.Job = cd.Job
where jm.udSyncToEcoSys = 'Y'
    and cd.[Source] in ('AP Entry', 'JC CostAdj', 'EMRev', 'PR Entry', 'JC MatUse', 'MS Tickets', 'IN MatlOrd',
					'AR Receipt', 'SM WorkOrd','PO Receipt')
    and cd.Mth = '4/1/2020'



