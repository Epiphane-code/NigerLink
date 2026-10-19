import 'package:e_services_niger/controllers/localisation_controller.dart';
import 'package:e_services_niger/controllers/provider_controller.dart';
import 'package:e_services_niger/models/coordonnee.dart';
import 'package:e_services_niger/views/widgets/carte_filter.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

class CarteMaps extends StatefulWidget {
  const CarteMaps({super.key});

  @override
  State<CarteMaps> createState() => _CarteMapsState();
}

class _CarteMapsState extends State<CarteMaps> {
  String filtreSelectionne = 'tous';

  @override
  void initState() {
    super.initState();

    WidgetsBinding.instance.addPostFrameCallback((_) {
      context.read<LocalisationController>().getCurrentCity();
      context.read<ProviderController>().getCoordonnees();
      context.read<ProviderController>().getServices();
    });
  }

  List<CoordonneeLatLnt> getLieuxFiltres({
    required String categorie,
    required List<CoordonneeLatLnt> lieux,
    required List<CoordonneeLatLnt> pharmaciesGarde,
  }) {
    // Afficher tous les lieux
    if (categorie == 'tous') {
      return lieux;
    }

    // Afficher uniquement les pharmacies de garde
    if (categorie == 'pharmacie de garde') {
      return pharmaciesGarde;
    }

    // Afficher les lieux d'une catégorie
    return lieux.where((item) => item.categorie == categorie).toList();
  }

  List<CoordonneeLatLnt> getPharmaciesGarde({
    required List<CoordonneeLatLnt> lieux,
    required List services,
  }) {
    final pharmaciesGardeCoordonnees = <CoordonneeLatLnt>[];

    for (final service in services) {
      // Vérifier que le service est une pharmacie de garde
      if (service.gardeVal == true && service.sousCategorieVal == 'pharmacie') {
        // Chercher la coordonnée correspondant au service
        for (final coordonnee in lieux) {
          if (coordonnee.nomId == service.idVal) {
            pharmaciesGardeCoordonnees.add(coordonnee);
            break;
          }
        }
      }
    }

    return pharmaciesGardeCoordonnees;
  }

  @override
  Widget build(BuildContext context) {
    final localisationController = context.watch<LocalisationController>();

    final providerController = context.watch<ProviderController>();

    final maPosition = localisationController.maPosition;

    final lieux = providerController.coordonnees;
    final List<String> categories = [
      'tous',
      'pharmacie',
      'pharmacie de garde',
      'sante',
      'ecole',
      'mosquee',
      'eglise',
      'ministere',
      'banque',
    ];
    if (maPosition == null) {
      return const Scaffold(body: Center(child: CircularProgressIndicator()));
    }
    final pharmaciesGardeCoordonnees = getPharmaciesGarde(
      lieux: lieux,
      services: providerController.services,
    );
    final lieuxFiltres = getLieuxFiltres(
      categorie: filtreSelectionne,
      lieux: lieux,
      pharmaciesGarde: pharmaciesGardeCoordonnees,
    );

    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'Rechercher sur la carte',
          style: TextStyle(color: Colors.white),
        ),
        backgroundColor: const Color(0xFF007A4D),
        automaticallyImplyLeading: false,
        actions: [
          IconButton(
            onPressed: () {
              Navigator.pop(context);
            },
            icon: const Icon(Icons.close, color: Colors.white),
          ),
        ],
      ),

      body: Column(
        children: [
          SizedBox(
            height: 55,
            child: ListView.builder(
              scrollDirection: Axis.horizontal,
              itemCount: categories.length,
              itemBuilder: (context, index) {
                final categorie = categories[index];

                return Padding(
                  padding: const EdgeInsets.all(5),

                  child: ChoiceChip(
                    label: Text(categorie.toUpperCase()),

                    selected: filtreSelectionne == categorie,

                    onSelected: (_) {
                      setState(() {
                        filtreSelectionne = categorie;
                      });
                    },
                  ),
                );
              },
            ),
          ),
          Expanded(
            child: CarteFilter(
              coordonneesList: lieuxFiltres,
              maPosition: maPosition,
            ),
          ),
        ],
      ),
    );
  }
}
