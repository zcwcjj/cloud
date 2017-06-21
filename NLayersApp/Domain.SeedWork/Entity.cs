using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Domain.SeedWork
{
    public abstract class Entity
    {
        int _id;

        public int Id {

            get { return _id;}
            set { _id = value;}
        }
    }
}
