from rest_framework import serializers

from .models import ContactInfo, Product, RetailNode


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class RetailNodeListSerializer(serializers.ModelSerializer):
    contacts = ContactInfoSerializer()

    class Meta:
        model = RetailNode
        exclude = ["debt"]

    def create(self, validated_data):
        contact_data = validated_data.pop("contacts")
        contact = ContactInfo.objects.create(**contact_data)
        return RetailNode.objects.create(contacts=contact, **validated_data)

    def update(self, instance, validated_data):
        contact_data = validated_data.pop("contacts", None)
        if contact_data:
            for attr, value in contact_data.items():
                setattr(instance.contacts, attr, value)
            instance.contacts.save()
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class RetailNodeDetailSerializer(serializers.ModelSerializer):
    contacts = ContactInfoSerializer()
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = RetailNode
        fields = "__all__"
        read_only_fields = ["debt"]
