from pydantic import BaseModel, validator, StrictStr, conlist
from typing import Dict, FrozenSet, List, Optional, Sequence, Set, Tuple, Union

class Inputscheck(BaseModel):
    
    yearlist: conlist(int, min_items=1, max_items=400)
    techlist: conlist(str, min_items=0, max_items=400)
    maxcapinvestment: conlist(float, min_items=0, max_items=400)
    mincapinvestment: conlist(float, min_items=0, max_items=400)
    mincap: conlist(float, min_items=0, max_items=400)
    annactlowlim: conlist(float, min_items=0, max_items=400)
    annactupplim: conlist(float, min_items=0, max_items=400)
    modperactlowlim: conlist(float, min_items=0, max_items=400)
    modperactupplim: conlist(float, min_items=0, max_items=400)
    rescap: conlist(float, min_items=0, max_items=400)
    maxcap: conlist(float, min_items=0, max_items=400)
    resstocap: conlist(float, min_items=0, max_items=400)
    maxstocap: conlist(float, min_items=0, max_items=400)
    stolevelstart: conlist(float, min_items=0, max_items=400)
    stolist: conlist(str, min_items=0, max_items=400)
    MOOLIST: conlist(str, min_items=1, max_items=2)
    STOLIST: conlist(str, min_items=0, max_items=400)
    listcf: conlist(str, min_items=0, max_items=400)
    listcfcheck: conlist(str, min_items=0, max_items=400)
    cftechlist: conlist(str, min_items=0, max_items=400) 
    setstechlist: conlist(str, min_items=0, max_items=400)
    listspd: conlist(str, min_items=0, max_items=400)
    listspdprof: conlist(str, min_items=0, max_items=400)
    listcfcap: conlist(str, min_items=0, max_items=400)
                

    @validator('STOLIST')
    def check1(cls, v, values, **kwargs):
        if len(v)!= 0 and len(values['MOOLIST'])!= 2:
            raise ValueError("Please make sure that there are two modes of operation if Storage is used in the model")
        return (v)


    @validator('maxstocap')
    def check3(cls, v, values, **kwargs):
        for i in range(0, len(values['resstocap'])):
            if values['resstocap'][i] > v[i]:
                raise ValueError("Please make sure that the residual storage capacity is less than the maximum allowed storage capacity")
        return (v)
    
    @validator('stolevelstart')
    def check30(cls, v, values, **kwargs):
        for i in range(0, len(values['maxstocap'])):
            if values['maxstocap'][i] < v[i]:
                raise ValueError("Please make sure that the storage starting level is less than the maximum allowed storage capacity")
        return (v)
    
    @validator('maxcap')
    def check4(cls, v, values, **kwargs):
        for i in range(0, len(values['techlist'])):
            if values['rescap'][i] > v[i]:
                raise ValueError("Please make sure that the residual capacity is less than the maximum allowed technology capacity")
        return (v)
    
    @validator('mincapinvestment')
    def check5(cls, v, values, **kwargs):
        for i in range(0, len(values['techlist'])):
            if values['maxcapinvestment'][i] < v[i]:
                raise ValueError("Please make sure that the minimum capacity addition is less than the maximum allowed capacity addition")
        return (v)
    
    @validator('mincap')
    def check6(cls, v, values, **kwargs):
        for i in range(0, len(values['techlist'])):
            if values['maxcapinvestment'][i] < v[i]:
                raise ValueError("Please make sure that the minimum capacity addition is less than the maximum allowed capacity addition")
        return (v)
    
    @validator('maxcap')
    def check7(cls, v, values, **kwargs):
        print(v)
        for i in range(0, len(values['techlist'])):
            if values['mincap'][i] > v[i]:
                raise ValueError("Please make sure that the minimum capacity addition is less than the maximum allowed capacity addition")
        return (v)
    
    @validator('annactupplim')
    def check8(cls, v, values, **kwargs):
        for i in range(0, len(values['techlist'])):
            if values['annactlowlim'][i] > v[i]:
                raise ValueError("Please make sure that the minimum annual heat generation is less than the maximum annual heat generation")
        return (v)
    
    @validator('maxcap')
    def check9(cls, v, values, **kwargs):
        for i in range(0, len(values['techlist'])):
            if values['rescap'][i] + values['mincapinvestment'][i] > v[i]:
                raise ValueError("Please make sure that the sum of minimum capacity addition and the residual capcity is less than the maximum allowed capacity")
        return (v)
    
    @validator('modperactupplim')
    def check10(cls, v, values, **kwargs):
        for i in range(0, len(values['techlist'])):
            if values['annactlowlim'][i] > v[i]:
                raise ValueError("Please make sure that the minimum annual heat generation is less than the maximum allowed model period heat generation")
        return (v)
    
    @validator('modperactupplim')
    def check11(cls, v, values, **kwargs):
        for i in range(0, len(values['techlist'])):
            if values['modperactlowlim'][i] > v[i]:
                raise ValueError("Please make sure that the minimum model period heat generation is less than the maximum allowed model period heat generation")
        return (v)
    
    @validator('modperactupplim')
    def check12(cls, v, values, **kwargs):
        for i in range(0, len(values['techlist'])):
            if values['modperactlowlim'][i] * len(values['yearlist']) > v[i]:
                raise ValueError("Please make sure that the sum of minimum annual period heat generation over all years is less than the maximum allowed model period heat generation")
        return (v)
    
    @validator('maxcap')
    def check13(cls, v, values, **kwargs):
        for i in range(0, len(values['techlist'])):
            if values['mincapinvestment'][i] * len(values['yearlist']) > v[i]:
                raise ValueError("Please make sure that the sum of minimum annual period heat generation over all years is less than the maximum allowed model period heat generation")
        return (v)
                     
    @validator('listcfcheck')
    def check14(cls, v, values, **kwargs):
        for i in values['listcf']:
            if i not in v:
                raise ValueError("The structure of technologies input from CF module is incompatible with the TEO. Please make sure that strtcure of technologies_cf in corrected.")
        return (v)
                     
    @validator('setstechlist')
    def check15(cls, v, values, **kwargs):
        if len(values['techlist']) != len(v):
            raise ValueError("The structure of technologies input for platform is incompatible with the TEO. Please make sure that all technologies are included in technologies_cf in corrected.")
        return (v)
                     
    @validator('setstechlist')
    def check16(cls, v, values, **kwargs):
        if len(values['cftechlist']) != len(v):
            raise ValueError("The structure of technologies input from CF module is incompatible with the TEO. Please make sure that all technologies are included in technologies_cf in corrected")
        return (v)
                
    @validator('listspd')
    def check17(cls, v, values, **kwargs):
        for i in v:
            if 'dem' not in i:
                raise ValueError("The structure of demand input from the CF module is incompatible with the TEO. Please make sure that all demands are included in the right format.")
        return (v)
                     
    @validator('listspdprof')
    def check18(cls, v, values, **kwargs):
        for i in v:
            if 'dem' not in i:
                raise ValueError("The structure of demand input for CF module is incompatible with the TEO. Please make sure that all demands are included in the right format.")
        return (v)
                     
    @validator('listcfcap')
    def check19(cls, v, values, **kwargs):
        for i in v:
            if 'sou' not in i:
                raise ValueError("The structure of capacity factor input for CF module is incompatible with the TEO. Please make sure that all capacity factors are included in the right format.")
        return ()

