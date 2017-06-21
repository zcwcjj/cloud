using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Domain.SeedWork;
using Domain.MainBoundedContext.Resources;

namespace Domain.MainBoundedContext.EquipmentConfigModule.Aggregates.EqupmentClassAgg
{
    public class EquipmentClass:Entity
    {
        private ICollection<CollectionType> _collectionTypes;

        public string ClassName
        {
            get;
            private set;
        }

        public virtual ICollection<CollectionType> CollectionTypes
        {
            get {
            if (_collectionTypes == null)
                _collectionTypes = new HashSet<CollectionType>();
            return _collectionTypes;
            }
            set {
                _collectionTypes = new HashSet<CollectionType>(value);
            }
        }

        public CollectionType AddNewCollectionType(string collectionTypeName, CollectionType.DATATYPE dataType)
        {
            if (collectionTypeName.Equals(""))
            {
                throw new ArgumentException(Messages.exception_invalidForCollectionType);
            }

            CollectionType type = new CollectionType { 
                DataType = dataType ,
                TypeName = collectionTypeName };

            this.CollectionTypes.Add(type);
            return type;


        }

    }
}
