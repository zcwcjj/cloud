using Domain.SeedWork;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Domain.MainBoundedContext.EquipmentConfigModule.Aggregates.EqupmentClassAgg
{
    public class CollectionType
        :Entity
    {
        /// <summary>
        /// 支持的类型
        /// </summary>
        public enum DATATYPE
        {
            DOUBLETYPE,
            BOOLTYPE,
            STRINGTYPE,
            BINARYSTRINGTYPE,
        } ;

        public string TypeName { get;  set; }

        public DATATYPE DataType { get;set; }


        

        
        

    }
}
