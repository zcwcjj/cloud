using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Domain.MainBoundedContext.EquipmentConfigModule.Aggregates.EqupmentClassAgg;

namespace Domain.MainBoundedContext.Tests
{
    [TestClass]
    public class EquipmentClassAggTest
    {
        [TestMethod]
        [ExpectedException(typeof(ArgumentException))]
        public void TestAddNewCollectionType()
        {
            EquipmentClass equipmentClass = new EquipmentClass();
            equipmentClass.AddNewCollectionType("", CollectionType.DATATYPE.BOOLTYPE);
            
        }
    }
}
