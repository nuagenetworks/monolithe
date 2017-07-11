import {{ class_prefix }}Attribute from 'service/{{ class_prefix }}Attribute';
import {{ superclass_name }} from 'service/{{ superclass_name }}';
import {{ class_prefix }}Exception from 'service/{{ class_prefix }}Exception';

/* Represents an abstract named entity, with attributes name and description
*/

export default class {{ class_prefix }}AbstractNamedEntity extends {{ superclass_name }} {
    constructor(...args) {
        super(...args);
        this.defineProperties({
            name: null,
            description: null,
        });
    }

    static attributeDescriptors = {
        ...{{ superclass_name }}.attributeDescriptors,
        name: new {{ class_prefix }}Attribute({
            localName: 'name',
            attributeType: {{ class_prefix }}Attribute.ATTR_TYPE_STRING,
            isRequired: true,
            canOrder: true,
            canSearch: true,
        }),
        description: new {{ class_prefix }}Attribute({
            localName: 'description',
            attributeType: {{ class_prefix }}Attribute.ATTR_TYPE_STRING,
            canSearch: true,
        }),
    }

    get RESTName() {
        throw new {{ class_prefix }}Exception('Not implemented');
    }
}

